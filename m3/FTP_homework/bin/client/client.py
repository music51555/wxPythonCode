import socket
import sys
import os
import re
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login
from core import pause
from core import verify_file_md5
from setting import set_struct
from setting import set_file
from setting import set_md5
from setting import set_time
from setting import set_table
from setting import set_bar
from setting import set_init

class FTPClient:
    max_recv_size = 8192
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.encoding = sys.getdefaultencoding()

    def client_bind(self):
        try:
            self.client.connect((self.host,self.port))
        except OSError:
            print('服务端关闭，再您重启服务后，请重新启动客户端连接服务器')
            exit()

    def get(self,cmd,filename):
        pause_init = '%s/%s/%s' % (self.base_dir,'db','pause.init')

        get_file = '%s/%s/%s' % (self.base_dir,'download',filename)

        if not os.path.exists(get_file):
            self.client.send(cmd.encode(self.encoding))

            get_dict = set_struct.struct_unpack(self.client)
            if get_dict['get_status'] == False:
                print('抱歉，您的云盘中没有这个文件')
                return

            confirm_dict = {
                'confirm_get':True
            }
            set_struct.struct_pack(self.client,confirm_dict)

            print('正在下载文件...')
            set_bar.set_bar()
            f = set_file.write_file(get_file, 'wb')
            recv_size = 0
            self.downloading(f,recv_size,get_file,get_dict)
        else:
            self.client.send(cmd.encode(self.encoding))
            get_dict = set_struct.struct_unpack(self.client)
            if get_dict['get_status'] == False:
                print('抱歉，您的云盘中没有这个文件')
                return

            get_file_md5 = set_md5.set_file_md5(get_file)
            if get_file_md5 == get_dict['file_md5']:
                print('文件已存在，无需重复下载')
                confirm_dict = {
                    'confirm_get': False
                }
                set_struct.struct_pack(self.client,confirm_dict)
                return
            else:
                f, file_name, recv_size = self.check_get_pause(get_file,pause_init)
                confirm_dict = {
                    'confirm_get': True,
                    'is_pause_go': self.is_pause_go
                }
                set_struct.struct_pack(self.client,confirm_dict)
                self.downloading(f,int(recv_size),file_name,get_dict)

    def check_get_pause(self,get_file,pause_init):
        if os.path.exists(pause_init):
            recv_size = conf_obj.set_conf(
                {'file_name': get_file},'read_recv_size',pause_init)
            if recv_size:
                while True:
                    self.is_pause_go = input('该文件在下载过程中意外中断连接，'
                                             '是否继续下载，执行断点续传?[ y | n]>>>')
                    if self.is_pause_go in ['n', 'N', 'y', 'Y']:
                        if self.is_pause_go in ['y', 'Y']:
                            f, file_name = pause_obj.read_pause(
                                get_file,self.is_pause_go,'client')

                        if self.is_pause_go in ['n', 'N']:
                            f, file_name = pause_obj.read_pause(
                                get_file,self.is_pause_go,'client')
                            recv_size = 0
                        break
                    else:
                        print('您的输入有误，请重新输入')
                        continue
            if recv_size == None:
                f = set_file.write_file(get_file, 'wb')
                file_name = get_file
                recv_size = 0
            return f,file_name,recv_size

    def downloading(self,f,recv_size,get_file,get_dict,recv_data = b''):
        while recv_size < get_dict['file_size']:
            data = self.client.recv(self.max_recv_size)
            if not data:
                pause_obj.set_pause(get_file,recv_size,conf_obj,warnmsg = True)
                return

            recv_size += len(data)
            pause_obj.set_pause(get_file,recv_size,conf_obj,warnmsg = False)
            f.write(data)
            recv_data += data
            print('已接收%s，文件总大小%s' % (recv_size,get_dict['file_size']))
        f.close()
        verify_file_md5.verify_file_md5(get_dict, get_file)

    def put(self,cmd,filename):
        put_file = '%s/%s/%s' % (self.base_dir,'download',filename)
        puted_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,filename)

        if os.path.exists(put_file):
            self.client.send(cmd.encode(self.encoding))

            file_size = os.path.getsize(put_file)
            file_md5 = set_md5.set_file_md5(put_file)

            put_file_dict = {
                'file_name': filename,
                'file_size': file_size,
                'file_md5':file_md5,
                'put_time':str(set_time.set_time())
            }
            set_struct.struct_pack(self.client,put_file_dict)

            self.put_diff(put_file,file_size,put_file_dict)
        else:
            print('您的个人文件夹中没有该文件，请上传已有的文件')
            return

    def put_diff(self,put_file,file_size,put_file_dict):
        while True:
            put_status_dict = set_struct.struct_unpack(self.client)
            while True:
                print(put_status_dict['put_message'])
                if put_status_dict['is_choice'] == 'yes':
                    is_pause_go = input('>>>')

                if put_status_dict['put_status'] == False:
                    if put_status_dict['put_again'] == 'yes':
                        if is_pause_go in ['n', 'N', 'y', 'Y']:
                            diff_dict = {
                                'is_pause_go': is_pause_go
                            }
                            set_struct.struct_pack(self.client, diff_dict)
                            break
                        else:
                            print('您的输入有误，请重新输入')
                            continue
                    else:
                        return
                else:
                    self.puting(put_file,put_status_dict,file_size,put_file_dict)
                    return

    def puting(self,put_file,put_status_dict,file_size,put_file_dict):
        puted_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,put_file_dict['file_name'])

        f = set_file.read_file(put_file, 'rb')
        f.seek(put_status_dict['recv_size'])
        set_bar.set_bar()

        send_data = put_status_dict['recv_size']
        while True:
            try:
                for line in f:
                    self.client.send(line)
                    send_data += len(line)
                    print('发送数据包大小：%s, 文件总大小：%s' % (send_data, file_size))
                f.close()
                break
            except BrokenPipeError:
                print('服务端接收数据连接中断，客户端重置连接')
                self.client.close()
                self.client_bind()
                return
        f.close()
        verify_file_md5.verify_file_md5(put_file_dict, puted_file)

    def view(self,cmd,username):
        count = 1
        if username != self.username:
            print('您只能查看自己文件夹下的文件')
            return

        self.client.send(cmd.encode(self.encoding))
        view_info = set_struct.struct_unpack(self.client)

        if isinstance(view_info,list):
            print('您的云盘是空的，快去上传文件吧')

        if isinstance(view_info,dict):
            print('您的云盘文件如下：')
            total_list = []
            for file in view_info:
                row_list = []

                count = str(count)
                row_list.append(count)

                file_name = view_info[file]['file_name']
                row_list.append(file_name)

                file_size = round(view_info[file]['file_size']/ 1000000,2)
                row_list.append(str(file_size)+'MB')

                file_type = view_info[file]['file_name'].rsplit('.')[1]
                row_list.append(file_type)

                put_date = view_info[file]['put_date']
                row_list.append(put_date)

                total_list.append(row_list)
                count = int(count) + 1

            set_table.set_table(total_list)

    def ll(self,cmd):
        self.client.send(cmd.encode(self.encoding))
        file_list = set_struct.struct_unpack(self.client)
        if len(file_list) == 0:
            print('文件夹是空的')
            return
        else:
            print('文件列表如下：')
            for file in file_list:
                print(file)

    def cd(self,cmd,directory):
        root_directory = '%s/%s'%(self.base_dir,'share')
        root_directory_list = os.listdir(root_directory)
        if directory in root_directory_list or directory in ['/','..']:
            self.client.send(cmd.encode(self.encoding))
        else:
            print('没有找到%s'%directory)

    def pwd(self,cmd):
        self.client.send(cmd.encode(self.encoding))
        current_directory= set_struct.struct_unpack(self.client)
        print(current_directory)

    def cmd_search(self,cmd):
        if cmd.startswith('get') or cmd.startswith('put'):
            return '上传、下载文件，您可以使用[ get | put 文件名.文件类型]来执行'
        if cmd.startswith('view'):
            return '您可以使用[ view 您的登录用户名 ]来访问您的云盘空间'
        if cmd.startswith('cd'):
            return '您可以使用[ cd / ]前往云盘根目录，或使用[ cd alex ]的方式前往根目录下的个人云盘文件夹'
        if cmd.startswith('pwd'):
            return '使用[ pwd ]命令来查看您当前所在的文件夹路径'
        if cmd.startswith('pwd'):
            return '使用[ ll ]命令来查看当前文件夹下的所有文件'

    def run(self):
        while True:
            self.client_bind()

            try:
                self.username = login_obj.login(self.client)
            except KeyboardInterrupt:
                print('客户端中断连接')
                exit()

            while True:
                cmd = input('请输入命令[ get | put | view | cd | pwd | ll ]>>>:').strip()
                if not cmd:
                    continue

                r_file = re.search('[get|put] .*\..*', cmd)
                r_view = re.search('view .*', cmd)
                r_help = re.search('[get|put|view|cd|pwd|ll] --help',cmd)
                r_cd = re.search('cd .*', cmd)
                r_ll = re.search('ll', cmd)
                r_pwd = re.search('pwd', cmd)

                if r_help:
                    re_msg = self.cmd_search(cmd)
                    print(re_msg)
                    continue

                elif r_file or r_view or r_cd:
                    request_method = cmd.split()[0]
                    request_content = cmd.split()[1]
                    if hasattr(self, request_method):
                        func = getattr(self, request_method)
                        func(cmd, request_content)
                        continue

                elif r_ll or r_pwd:
                    request_method = cmd.split()[0]
                    if hasattr(self, request_method):
                        func = getattr(self, request_method)
                        func(cmd)
                        continue

                else:
                    print('命令格式错误,您可以使用[命令 --help]方式查看使用说明 ')
                    continue

if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8082)
    login_obj = login.UserBehavior()
    pause_obj = pause.Pause()
    conf_obj = set_init.set_Init()
    f.run()