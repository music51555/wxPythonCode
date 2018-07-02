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
                       issuccess = set_struct.struct_unpack(self.client)

                       if issuccess == True:
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

    def put(self,filename):
        put_file = '%s/%s/%s' % (self.base_dir, 'download', filename)
        if os.path.exists(put_file):
            file_size = os.path.getsize(put_file)
            file_md5 = set_md5.set_file_md5(put_file)

            put_file_dict = {
                'file_name': filename,
                'file_size': file_size,
                'file_md5':file_md5
            }

            set_struct.struct_pack(self.client,put_file_dict)
            put_dict = set_struct.struct_unpack(self.client)

            if put_dict['put_status'] == False:
                print(put_dict['put_message'])
                return

            f = set_file.read_file(put_file,'rb')
            for line in f:
                self.client.send(line)
        else:
            print('您的个人文件夹中没有该文件，请上传已有的文件')
            return

    def run(self):
        self.client_bind()
        self.login()
        while True:
            cmd = input('请输入命令>>>:')
            if not cmd:
                continue
            self.client.send(cmd.encode(self.encoding))
            if hasattr(self,cmd.split()[0]):
                request_method = cmd.split()[0]
                request_content = cmd.split()[1]

                func = getattr(self,request_method)
                func(request_content)
            else:
                print('您输入的命令有误，请重新输入>>>:')
                continue

if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8081)
    login_obj = login.UserBehavior()
    f.run()