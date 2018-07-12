import socket
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login
from core import pause
from core import verify_file_md5
from setting import set_struct
from setting import set_file
from setting import set_md5
from setting import set_init
from setting import set_bytes
from setting import set_time

class FTPServer:
    max_queue_size = 5
    max_recv_size = 8192
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root_directory = os.path.join(base_dir, 'share')
    current_directory = root_directory
    put_response_code = {
        '200': '请稍等,文件上传中...',
        '201': '您的云空间中已存在该文件',
        '202': '该文件在上传过程中意外中断连接,是否继续上传，执行断点续传?[ y | n ]>>>',
        '203': '客户端关闭，服务端重置连接',
        '204': '账户验证成功，服务端准备就绪...',
        '205': '账户验证失败，服务端重置连接...',
        '206': '客户端接收数据中断，服务端重置连接',
        '207': '下载任务完成'
    }

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.encoding = sys.getdefaultencoding()

    def server_bind(self):
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind((self.host,self.port))
        self.server.listen(self.max_queue_size)

    def server_accept(self):
        self.conn, self.caddr = self.server.accept()

        while True:
            login_info = set_struct.recv_message(self.conn)
            if login_info == None:
                break
            #验证帐号是否正确，将返回的结果True和False返回给客户端，客户端以此凭据来展示登录成功或失败
            is_success,self.username = login_obj.verify_account(login_info)
            is_success_dict = {
                'is_success':is_success,
                'username':self.username
            }
            set_struct.send_message(self.conn, is_success_dict)

            if is_success_dict['is_success'] == True:
                print(self.put_response_code['204'])
                return
            else:
                print(self.put_response_code['205'])
                continue

    @property
    def free_size(self):
        #获取用户云盘空间剩余容量的函数方法
        disk_size = conf_obj.get_size(self.username)
        share_file_list = os.listdir(os.path.join(self.base_dir,'share',self.username))

        if len(share_file_list) == 0:
            free_size = 104857600
        else:
            total_size = 0
            for file in share_file_list:
                total_size += os.path.getsize(os.path.join(self.base_dir,'share',self.username,file))
            free_size = int(disk_size) - total_size
        return free_size

    def size_not_enough(self,put_file_dict):
        #云盘空间不足，告知客户端的方法
        put_status_dict = {
            'put_status': False,
            'put_message': '很抱歉，您的云盘空间不足，剩余空间为%sMB,您上传附件的大小是%sMB'
                           % (set_bytes.set_bytes(self.free_size),
                              set_bytes.set_bytes(put_file_dict['file_size'])),
            'put_again': 'no',
            'is_choice': 'no'
        }
        set_struct.send_message(self.conn,put_status_dict)
        return

    def get(self, filename):
        #服务端接收get请求的方法，判断下载的文件是否存在
        #1、如果文件存在，会将文件信息以字典的形式发送给客户端
        #2、如果文件不存在，则会get_status设置为False
        geted_file = os.path.join(self.base_dir,'share',self.username,filename)
        pause_init = os.path.join(self.base_dir,'db','pause.init')
        get_file = os.path.join(self.base_dir,'download',filename)

        if os.path.exists(geted_file):
            file_size = os.path.getsize(geted_file)
            file_md5 = set_md5.set_file_md5(geted_file)

            get_dict = {
                'file_name':filename,
                'file_size':file_size,
                'file_md5':file_md5,
                'get_status':True
            }
            set_struct.send_message(self.conn,get_dict)
            confirm_dict = set_struct.recv_message(self.conn)
            if confirm_dict['confirm_get'] == False:
                return
            self.downloading(geted_file,pause_init,get_file,confirm_dict)
        else:
            get_dict = {
                'get_status':False
            }
            set_struct.send_message(self.conn,get_dict)

    def downloading(self,geted_file,pause_init,get_file,confirm_dict):
        #开始下载文件的函数方法
        f = set_file.read_file(geted_file, 'rb')
        if os.path.exists(pause_init):
            recv_size = conf_obj.set_conf(
                {'file_name': get_file}, 'read_recv_size', pause_init)

            if 'is_pause_go' in confirm_dict.keys():
                if confirm_dict['is_pause_go'] == 'y':
                    f.seek(int(recv_size))

        if confirm_dict['confirm_get'] == True:
            try:
                for line in f:
                    self.conn.send(line)
                print(self.put_response_code['207'])
            except BrokenPipeError:
                print(self.put_response_code['206'])
                self.conn.close()
                self.server_accept()
                return
            except ConnectionResetError:
                print(self.put_response_code['206'])
                self.conn.close()
                self.server_accept()
                return

    def put(self,filename):
        #服务端接收到put命令，处理上传文件的函数犯法
        #1、如果文件存在，则会调用check_put_pause方法，检查断点续传配置文件爱你
        #2、如果文件不存在，且磁盘空间满足上传文件的大小，则会调用puting方法执行上传
        put_file_dict = set_struct.recv_message(self.conn)
        puted_file = os.path.join(self.base_dir, 'share', self.username,filename)
        pause_init = os.path.join(self.base_dir, 'db', 'pause.init')

        if os.path.exists(puted_file):
            f,recv_size = self.check_put_pause(put_file_dict,puted_file,pause_init)
            if f == None:
                return
        else:
            f = None
            recv_size = 0

        if put_file_dict['file_size'] < self.free_size:
            put_status_dict = {
                'put_status': True,
                'put_message':self.put_response_code['200'],
                'put_again':'no',
                'is_choice': 'no',
                'recv_size':recv_size
            }
            set_struct.send_message(self.conn, put_status_dict)
            self.puting(f,recv_size,put_file_dict,puted_file)
        else:
            self.size_not_enough(put_file_dict)
        return

    def put_file_existed(self):
        #如果上传的文件已经存在，且MD5码一直，告知客户端文件已存在
            put_status_dict = {
                'put_status': False,
                'put_message': self.put_response_code['201'],
                'put_again': 'no',
                'is_choice': 'no'
            }
            set_struct.send_message(self.conn, put_status_dict)
            return None, None

    def check_put_pause(self,put_file_dict,puted_file,pause_init):
        #检查文件的MD5码
        #1、如果文件MD5码一致，则会调用put_file_existed方法告知客户端
        #2、如果MD5码不一致，且断点续传配置文件中也存在上传文件的断点记录的话，会让用户选择是否继续断点续传
        puted_file_md5 = set_md5.set_file_md5(puted_file)

        if puted_file_md5 == put_file_dict['file_md5']:
            f,recv_size = self.put_file_existed()
            return f,recv_size
        else:
            if os.path.exists(pause_init):
                recv_size = conf_obj.set_conf({'file_name': puted_file},
                                              'read_recv_size',
                                              pause_init)

                put_status_dict = {
                    'put_status': False,
                    'put_message':self.put_response_code['202'],
                    'put_again': 'yes',
                    'is_choice': 'yes'
                }
                set_struct.send_message(self.conn, put_status_dict)
                diff_dict = set_struct.recv_message(self.conn)

                if diff_dict['is_pause_go'] == 'y':
                    f = set_file.write_file(puted_file,'ab')

                if diff_dict['is_pause_go'] == 'n':
                    f = set_file.write_file(puted_file,'wb')
                    recv_size = 0

                return f,int(recv_size)

    def puting(self,f,recv_size,put_file_dict,puted_file):
        #执行上传文件的函数方法
        if f == None:
            f = set_file.write_file(puted_file, 'wb')
        while recv_size < put_file_dict['file_size']:
            data = self.conn.recv(self.max_recv_size)
            if not data:
                pause_obj.set_pause(puted_file, recv_size, conf_obj,
                                    warnmsg=True)
                self.conn.close()
                self.server_accept()
                return
            recv_size += len(data)
            pause_obj.set_pause(puted_file, recv_size, conf_obj,
                                warnmsg=False)
            f.write(data)
        f.close()
        verify_file_md5.verify_file_md5(put_file_dict, puted_file)

    def view(self,username):
        view_dict = {}
        share_file_list = os.listdir(os.path.join(self.base_dir,'share',username))[:]
        #通过view命令浏览云盘文件，返回文件的名称、大小、上传日期等属性
        if len(share_file_list) == 0:
            set_struct.send_message(self.conn, share_file_list)
        else:
            for file in share_file_list:
                view_dict[file] = {
                    'file_name':file,
                    'file_size':
                        os.path.getsize(
                            os.path.join(self.base_dir,'share',username,file)),
                    'put_date':
                        set_time.set_time(os.path.getctime(
                            os.path.join(self.base_dir,'share',username,file)))
                }
            set_struct.send_message(self.conn,view_dict)

    def ll(self):
        files_list = os.listdir(self.current_directory)
        for file in files_list:
            print(os.stat(os.path.join(self.current_directory,file)))
        set_struct.send_message(self.conn, files_list)

    def pwd(self):
        set_struct.send_message(self.conn, self.current_directory)

    def cd(self,user_home):
        #通过cd命令切换目录
        if user_home not in ['/','..']:
            self.user_directory = os.path.join(self.base_dir,'share',user_home)

        if user_home == '/':
            self.current_directory = self.root_directory
            set_struct.send_message(self.conn,self.current_directory)
        elif user_home == '..':
            if self.current_directory == self.root_directory:
                self.current_directory = self.root_directory
                set_struct.send_message(self.conn, self.current_directory)
                return

            if self.current_directory == self.user_directory:
                self.current_directory = self.root_directory
                set_struct.send_message(self.conn, self.current_directory)

        elif user_home in os.listdir(self.current_directory):
            self.current_directory = self.user_directory
            set_struct.send_message(self.conn,self.current_directory)

    def run(self):
        self.server_bind()
        while True:
            self.server_accept()
            while True:
                cmd = self.conn.recv(self.max_recv_size)
                if not cmd:
                    print(self.put_response_code['203'])
                    break

                request_method = cmd.decode(self.encoding).split()[0]

                if hasattr(self,request_method):
                    #不同长度的命令分别处理，需要该判断，因为调用函数时传递的参数不同
                    if len(cmd.decode(self.encoding).split()) == 2:
                        request_content = cmd.decode(self.encoding).split()[1]
                        func = getattr(self, request_method)
                        func(request_content)
                        continue
                    else:
                        func = getattr(self, request_method)
                        func()
                        continue

                self.conn.close()

if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8082)
    print('请先登录...')
    login_obj = login.UserBehavior()
    pause_obj = pause.Pause()
    conf_obj = set_init.set_Init()
    f.run()




