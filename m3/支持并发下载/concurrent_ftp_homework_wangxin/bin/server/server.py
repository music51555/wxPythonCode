import socket
import sys
import os
import select

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
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import queue

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
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.encoding = sys.getdefaultencoding()

    def server_bind(self):
        self.server.bind((self.host,self.port))
        self.server.listen(self.max_queue_size)
        self.server.setblocking(False)

    def login(self,sock,wdata):
        while True:
            try:
                login_info = set_struct.recv_message(sock)
                if login_info == None:
                    break
            except BlockingIOError:
                continue
            #z在客户端登录时如果失去连接，那么会导致服务端也会被终止，在此捕获异常
            except ConnectionResetError:
                queue.get()
                break
            #验证帐号是否正确，将返回的结果True和False返回给客户端，客户端以此凭据来展示登录成功或失败
            is_success,username = login_obj.verify_account(login_info)
            wdata[sock] = [username,]
            is_success_dict = {
                'is_success':is_success,
                'username':username
            }
            set_struct.send_message(sock, is_success_dict)

            if is_success_dict['is_success'] == True:
                print(self.put_response_code['204'])
                return
            else:
                print(self.put_response_code['205'])
                continue

    def free_size(self,sock,wdata):
        #获取用户云盘空间剩余容量的函数方法
        disk_size = conf_obj.get_size(wdata[sock][0])
        share_file_list = os.listdir(os.path.join(self.base_dir,'share',wdata[sock][0]))

        if len(share_file_list) == 0:
            free_size = 104857600
        else:
            total_size = 0
            for file in share_file_list:
                total_size += os.path.getsize(os.path.join(self.base_dir,'share',wdata[sock][0],file))
            free_size = int(disk_size) - total_size
        return free_size

    def size_not_enough(self,put_file_dict,sock,wdata):
        free_size = self.free_size(sock,wdata)
        #云盘空间不足，告知客户端的方法
        put_status_dict = {
            'put_status': False,
            'put_message': '很抱歉，您的云盘空间不足，剩余空间为%sMB,您上传附件的大小是%sMB'
                           % (set_bytes.set_bytes(free_size),
                              set_bytes.set_bytes(put_file_dict['file_size'])),
            'put_again': 'no',
            'is_choice': 'no'
        }
        set_struct.send_message(sock,put_status_dict)
        return

    def get(self, filename,sock,wdata,rlist):
        #服务端接收get请求的方法，判断下载的文件是否存在
        #1、如果文件存在，会将文件信息以字典的形式发送给客户端
        #2、如果文件不存在，则会get_status设置为False
        geted_file = os.path.join(self.base_dir,'share',wdata[sock][0],filename)
        pause_init = os.path.join(self.base_dir,'db','pause.init')
        get_file = os.path.join(self.base_dir,'download',wdata[sock][0],filename)

        if os.path.exists(geted_file):
            file_size = os.path.getsize(geted_file)
            file_md5 = set_md5.set_file_md5(geted_file)

            get_dict = {
                'file_name':filename,
                'file_size':file_size,
                'file_md5':file_md5,
                'get_status':True
            }
            set_struct.send_message(sock, get_dict)

            pool = ThreadPoolExecutor()
            confirm_dict = pool.submit(set_struct.recv_message,sock).result()
            print(confirm_dict)
            if confirm_dict['confirm_get'] == False:
                return
            t = Thread(target = self.downloading,args = (geted_file,pause_init,get_file,confirm_dict,sock,wdata,rlist))
            t.start()

        else:
            get_dict = {
                'get_status':False
            }
            set_struct.send_message(sock,get_dict)

    def downloading(self,geted_file,pause_init,get_file,confirm_dict,sock,wdata,rlist):
        print('filename',get_file)
        #开始下载文件的函数方法
        f = set_file.read_file(geted_file, 'rb')
        if os.path.exists(pause_init):
            print('readle')
            recv_size = conf_obj.set_conf(
                {'file_name': get_file}, 'read_recv_size', pause_init)

            if 'is_pause_go' in confirm_dict.keys():
                if confirm_dict['is_pause_go'] == 'y':
                    f.seek(int(recv_size))
                    print(recv_size)

        if confirm_dict['confirm_get'] == True:
            try:
                for line in f:
                    while True:
                        try:
                            sock.send(line)
                            break
                        except BlockingIOError:
                            continue
                print(self.put_response_code['207'])
                file_size = os.path.getsize(get_file)
                pause_obj.set_pause(get_file, file_size, conf_obj, warnmsg=False)
                f.close()
                rlist.append(sock)
            except Exception:
                queue.get()
                file_size = os.path.getsize(get_file)
                pause_obj.set_pause(get_file, file_size, conf_obj, warnmsg=False)
                print(self.put_response_code['206'])
                sock.close()

    def put(self,filename,sock,wdata,rlist):
        print('jin')
        #服务端接收到put命令，处理上传文件的函数犯法
        #1、如果文件存在，则会调用check_put_pause方法，检查断点续传配置文件爱你
        #2、如果文件不存在，且磁盘空间满足上传文件的大小，则会调用puting方法执行上传
        put_file_dict = set_struct.recv_message(sock)
        print('put_file_dict',put_file_dict)
        puted_file = os.path.join(self.base_dir, 'share', wdata[sock][0],filename)
        pause_init = os.path.join(self.base_dir, 'db', 'pause.init')
        free_size = self.free_size(sock,wdata)

        if os.path.exists(puted_file):
            f,recv_size = self.check_put_pause(put_file_dict,puted_file,pause_init,sock)
            if f == None:
                return
        else:
            f = None
            recv_size = 0

        if put_file_dict['file_size'] < free_size:
            put_status_dict = {
                'put_status': True,
                'put_message':self.put_response_code['200'],
                'put_again':'no',
                'is_choice': 'no',
                'recv_size':recv_size
            }
            set_struct.send_message(sock, put_status_dict)

            t = Thread(target = self.puting,args = (f,recv_size,put_file_dict,puted_file,sock,rlist))
            t.start()
            t.join()
        else:
            self.size_not_enough(put_file_dict,sock,wdata)

    def put_file_existed(self,sock):
        #如果上传的文件已经存在，且MD5码一直，告知客户端文件已存在
            put_status_dict = {
                'put_status': False,
                'put_message': self.put_response_code['201'],
                'put_again': 'no',
                'is_choice': 'no'
            }
            set_struct.send_message(sock, put_status_dict)
            return None, None

    def check_put_pause(self,put_file_dict,puted_file,pause_init,sock):
        #检查文件的MD5码
        #1、如果文件MD5码一致，则会调用put_file_existed方法告知客户端
        #2、如果MD5码不一致，且断点续传配置文件中也存在上传文件的断点记录的话，会让用户选择是否继续断点续传
        puted_file_md5 = set_md5.set_file_md5(puted_file)

        if puted_file_md5 == put_file_dict['file_md5']:
            f,recv_size = self.put_file_existed(sock)
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
                set_struct.send_message(sock, put_status_dict)
                diff_dict = set_struct.recv_message(sock)

                if diff_dict['is_pause_go'] == 'y':
                    f = set_file.write_file(puted_file,'ab')

                if diff_dict['is_pause_go'] == 'n':
                    f = set_file.write_file(puted_file,'wb')
                    recv_size = 0

                return f,int(recv_size)

    def puting(self,f,recv_size,put_file_dict,puted_file,sock,rlist):
        #执行上传文件的函数方法
        if f == None:
            f = set_file.write_file(puted_file, 'wb')
        while recv_size < put_file_dict['file_size']:
            try:
                data = sock.recv(self.max_recv_size)
            except BlockingIOError:
                continue
            if not data:
                pause_obj.set_pause(puted_file, recv_size, conf_obj,
                                    warnmsg=True)
                sock.close()
                return
            recv_size += len(data)

            f.write(data)
        pause_obj.set_pause(puted_file, recv_size, conf_obj,warnmsg=False)
        f.close()
        verify_file_md5.verify_file_md5(put_file_dict, puted_file)
        rlist.append(sock)

    def view(self,sock,wdata,rlist):
        view_dict = {}
        share_file_list = os.listdir(os.path.join(self.base_dir,'share',wdata[sock][0]))[:]
        #通过view命令浏览云盘文件，返回文件的名称、大小、上传日期等属性
        if len(share_file_list) == 0:
            set_struct.send_message(sock, share_file_list)
        else:
            for file in share_file_list:
                view_dict[file] = {
                    'file_name':file,
                    'file_size':
                        os.path.getsize(
                            os.path.join(self.base_dir,'share',wdata[sock][0],file)),
                    'put_date':
                        set_time.set_time(os.path.getctime(
                            os.path.join(self.base_dir,'share',wdata[sock][0],file)))
                }
            set_struct.send_message(sock,view_dict)
        rlist.append(sock)

    def ll(self,sock,wdata,rlist):
        #浏览当前文件夹下文件的方法
        files_list = os.listdir(self.current_directory)
        for file in files_list:
            print(os.stat(os.path.join(self.current_directory,file)))
        set_struct.send_message(sock, files_list)
        rlist.append(sock)

    def pwd(self,sock,wdata,rlist):
        #查看当前所在路径的方法
        set_struct.send_message(sock, self.current_directory)
        rlist.append(sock)

    def cd(self,request_content,sock,wdata,rlist):
        #通过cd命令切换目录
        if request_content not in ['/','..']:
            self.user_directory = os.path.join(self.base_dir,'share',wdata[sock][0])

        if request_content == '/':
            self.current_directory = self.root_directory
            set_struct.send_message(sock,self.current_directory)
            rlist.append(sock)

        elif request_content == '..':
            if self.current_directory == self.root_directory:
                self.current_directory = self.root_directory
                set_struct.send_message(sock, self.current_directory)
                rlist.append(sock)

            if self.current_directory == self.user_directory:
                self.current_directory = self.root_directory
                set_struct.send_message(sock, self.current_directory)
                rlist.append(sock)

        elif request_content in os.listdir(self.current_directory):
            self.current_directory = self.user_directory
            set_struct.send_message(sock,self.current_directory)
            rlist.append(sock)

    def run(self):
        link_status_file = os.path.join(self.base_dir,'db','link_status.txt')
        self.server_bind()
        conn_is_login = []
        conn_not_login = []
        rlist = [self.server,]
        wlist = []
        wdata = {}
        while True:
            rl,wl,xl = select.select(rlist,wlist,[],0.5)
            for sock in rl:
                if sock == self.server:
                    conn, caddr = self.server.accept()
                    #如果有客户端连接，如果队列没有满，则放入caddr，放入后如果队列满，则会创建文件，该文件的存在与否表示队列是否满载
                    if conn:
                        if not queue.full():
                            queue.put(caddr)
                            if queue.full():
                                set_file.write_file(link_status_file, 'w')
                        if queue.empty():
                            os.remove(link_status_file)
                    rlist.append(conn)
                    conn_not_login.append(conn)
                else:
                    if sock in conn_not_login:
                        t = Thread(target=self.login, args=(sock,wdata))
                        t.start()
                        t.join()
                        conn_is_login.append(sock)
                        conn_not_login.remove(sock)
                        break
                    while True:
                        try:
                            cmd_dict = set_struct.recv_message(sock)
                            cmd = cmd_dict['cmd']
                            if not cmd:
                                queue.get()
                                os.remove(link_status_file)
                                print(self.put_response_code['203'])
                                sock.close()
                                rlist.remove(sock)
                                wdata.pop(sock)
                                break
                            wlist.append(sock)
                            wdata[sock].append(cmd)
                            break
                        except BlockingIOError:
                            break
                        except Exception:
                            queue.get()
                            #通过文件是否存在控制并发量，如果客户端断开则删除该文件，表示允许客户端连接
                            if os.path.exists(link_status_file):
                                os.remove(link_status_file)
                            print(self.put_response_code['203'])
                            sock.close()
                            #在客户端登录时，还没有获取到rlist和wdata的值，所以当客户端重新连接时，服务端会报错
                            try:
                                rlist.remove(sock)
                                wdata.pop(sock)
                            except KeyError:
                                break
                            break

            for sock in wl:
                request_method = wdata[sock][1].split()[0]

                if hasattr(self,request_method):
                    #不同长度的命令分别处理，需要该判断，因为调用函数时传递的参数不同
                    if len(wdata[sock][1].split()) == 2:
                        request_content = wdata[sock][1].split()[1]
                        func = getattr(self, request_method)
                        #从之前的通过反射判断如果方法存在，那么就执行func()变为发起一个线程去执行这个方法
                        t = Thread(target = func,args = (request_content,sock,wdata,rlist))
                        t.start()
                        rlist.remove(sock)
                        wlist.remove(sock)
                        #之前没加这一句，下载的都是同一个文件
                        del wdata[sock][1]
                    else:
                        func = getattr(self, request_method)
                        t = Thread(target = func,args = (sock,wdata,rlist))
                        t.start()
                        rlist.remove(sock)
                        wlist.remove(sock)
                        del wdata[sock][1]

if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8081)
    print('请先登录...')
    login_obj = login.UserBehavior()
    pause_obj = pause.Pause()
    conf_obj = set_init.set_Init()
    queue = queue.Queue(2)
    f.run()


