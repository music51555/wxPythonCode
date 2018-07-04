import socket
import sys
import os
import json
import struct

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login
from setting import set_struct
from setting import set_file
from setting import set_md5

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
                set_struct.struct_pack(file_diff)
                break
            else:
                print('您的输入有误，请重新输入')
                continue

    def put(self,cmd,filename):
        put_file = '%s/%s/%s' % (self.base_dir, 'download', filename)

        if os.path.exists(put_file):
            self.client.send(cmd.encode(self.encoding))

            file_size = os.path.getsize(put_file)
            file_md5 = set_md5.set_file_md5(put_file)

            put_file_dict = {
                'file_name': filename,
                'file_size': file_size,
                'file_md5':file_md5
            }
            set_struct.struct_pack(self.client,put_file_dict)

            while True:
                put_dict = set_struct.struct_unpack(self.client)
                print(put_dict['put_message'])

                if put_dict['put_status'] == False:
                    if put_dict['put_again'] == 'yes':
                        self.file_diff()
                    else:
                        return
                else:
                    f = set_file.read_file(put_file,'rb')
                    for line in f:
                        self.client.send(line)
                    print('文件上传成功')
                    return
        else:
            print('您的个人文件夹中没有该文件，请上传已有的文件')
            return

    def view(self,cmd,username):
        if username != self.username:
            print('您只能查看自己文件夹下的文件')
            return
        self.client.send(cmd.encode(self.encoding))
        share_file_list = set_struct.struct_unpack(self.client)
        print('您的云盘文件如下：')
        for file in share_file_list:
            print(file)


    def run(self):
        self.client_bind()
        self.login()
        while True:
            cmd = input('请输入命令[ get | put | view ]>>>:').strip()
            if not cmd:
                continue
            if hasattr(self,cmd.split()[0]):
                request_method = cmd.split()[0]
                request_content = cmd.split()[1]

                func = getattr(self,request_method)
                func(cmd,request_content)
            else:
                print('您输入的命令有误，请重新输入>>>:')
                continue

if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8081)
    login_obj = login.UserBehavior()
    f.run()