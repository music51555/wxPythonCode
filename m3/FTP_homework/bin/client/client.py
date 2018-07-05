import socket
import sys
import os
import json
import struct
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login
from setting import set_struct
from setting import set_file
from setting import set_md5
from setting import set_time
from setting import set_table
from setting import set_bar

class FTPClient:
    max_recv_size = 8192
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.encoding = sys.getdefaultencoding()

    def login(self):
        while True:
            login_choice = input('还没有账号？按r注册账号，已有账号请按g>>>：')
            if login_choice in ['r', 'R', 'g', 'G']:

                if login_choice in ['r', 'R']:
                    login_obj.register()
                    continue

                if login_choice in ['g', 'G']:
                    if not os.path.exists('%s/%s/%s' % (self.base_dir, 'db', 'account.init')):
                        print('当前系统内还没有任何账号，请先注册')
                        continue

                    while True:
                       username = input('请输入用户名：')
                       password = input('请输入密码：')

                       login_info = {
                           'username': username,
                           'password': password
                       }

                       set_struct.struct_pack(self.client,login_info)
                       is_success_dict = set_struct.struct_unpack(self.client)

                       if is_success_dict['is_success'] == True:
                           self.username = is_success_dict['username']
                           print('登录成功')
                           return
                       else:
                           print('用户名或密码错误，请重新输入')
                           continue
            else:
                print('您的输入有误，请重新输入')
                continue

    def client_bind(self):
        self.client.connect((self.host,self.port))

    def file_diff(self):
        while True:
            set_diff = input('确认上传将覆盖已有文件,覆盖已有云盘文件请按y，建立新的同名文件请按n>>>')
            if set_diff in ['y', 'Y', 'n', 'N']:
                file_diff = {
                    'set_diff': set_diff
                }
                set_struct.struct_pack(self.client,file_diff)
                break
            else:
                print('您的输入有误，请重新输入')
                continue

    def get(self,cmd,filename):
        print('进来了啊')
        get_file = '%s/%s/%s' % (self.base_dir, 'download', filename)


        if not os.path.exists(get_file):
            self.client.send(cmd.encode(self.encoding))

            get_dict = set_struct.struct_unpack(self.client)
            if get_dict['get_status'] == False:
                print('抱歉，您要下载的文件不存在')
                return
            confirm_get_dict = {
                'confirm_get':True
            }

            f = set_file.write_file(get_file,'wb')

            set_struct.struct_pack(self.client,confirm_get_dict)

            recv_size = 0
            set_bar.set_bar()
            print('正在下载文件...')
            while recv_size < get_dict['file_size']:
                data = self.client.recv(self.max_recv_size)
                f.write(data)
                recv_size += len(data)
                print('已接收%s，文件总大小%s'%(recv_size,get_dict['file_size']))
            f.close()
            get_file_md5 = set_md5.set_file_md5(get_file)
            print(get_file_md5)
            if get_file_md5 == get_dict['file_md5']:
                print('文件下载完成，校验MD5一致')
        else:
            get_dict = set_struct.struct_unpack(self.client)

            confirm_get_dict = {
                'confirm_get': False
            }

            set_struct.struct_pack(self.client, confirm_get_dict)

            get_file_md5 = set_md5.set_file_md5(get_file)
            if get_file_md5 == get_dict['file_md5']:
                print('文件已存在，无需重复下载')
                return

    def put(self,cmd,filename):
        put_file = '%s/%s/%s' % (self.base_dir, 'download', filename)

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

            while True:
                put_status_dict = set_struct.struct_unpack(self.client)
                print(put_status_dict['put_message'])

                if put_status_dict['put_status'] == False:
                    if put_status_dict['put_again'] == 'yes':
                        self.file_diff()
                    else:
                        return
                else:
                    put_file_dict['file_size'] / 1024 / 60
                    f = set_file.read_file(put_file,'rb')

                    while True:
                        set_bar.set_bar()
                        for line in f:
                            self.client.send(line)
                        break
                    print('文件上传成功')
                    return
        else:
            print('您的个人文件夹中没有该文件，请上传已有的文件')
            return

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

    def run(self):
        self.client_bind()
        self.login()
        while True:
            cmd = input('请输入命令[ get | put | view ]>>>:').strip()
            if not cmd:
                continue
            r_file = re.search('[get|put] .*\..*', cmd)
            r_view = re.search('view .*', cmd)
            r_help = re.search('[get|put|view] --help',cmd)
            if r_help:
                if cmd.startswith('get') or cmd.startswith('put'):
                    print('上传、下载文件，您可以使用[get|put 文件名.文件类型]来执行')
                if cmd.startswith('view'):
                    print('您可以使用[view 您的登录用户名]来访问您的云盘空间')
                continue

            elif r_file:
                request_method = cmd.split()[0]
                filename = cmd.split()[1]
                if hasattr(self, cmd.split()[0]):
                    func = getattr(self, request_method)
                    func(cmd, filename)
                    continue

            elif r_view:
                request_method = cmd.split()[0]
                filename = cmd.split()[1]
                if hasattr(self, cmd.split()[0]):
                    func = getattr(self, request_method)
                    func(cmd, filename)
                    continue

            else:
                print('命令格式错误,您可以使用[命令 --help]方式查看使用说明 ')
                continue


if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8081)
    login_obj = login.UserBehavior()
    f.run()