import socket
import sys
import os
import json
import struct

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login

class FTPClient:
    max_recv_size = 8192

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def login(self):
        while True:
            login_choice = input('还没有账号？按r注册账号，已有账号请按g>>>：')
            if login_choice in ['r', 'R', 'g', 'G']:
                if login_choice in ['r', 'R']:
                    loginobj.register()
                    continue
                if login_choice in ['g', 'G']:
                    username = input('请输入用户名：')
                    password = input('请输入密码：')

                    login_info = {
                        'username': username,
                        'password': password
                    }
                    login_bytes = json.dumps(login_info).encode('utf-8')
                    self.client.send(struct.pack('i', len(login_bytes)))
            else:
                print('您的输入有误，请重新输入')
                continue

    def client_bind(self):
        self.client.connect((self.host,self.port))

    def run(self):
        self.client_bind()
        self.login()
        cmd = input('请输入命令>>>:')


if __name__ == '__main__':
    f = FTPClient('127.0.0.1',8080)
    loginobj = login.UserBehavior()
    f.run()