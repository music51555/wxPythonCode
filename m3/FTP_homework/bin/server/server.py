import socket
import sys
import os
import struct

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from core import login

class FTPServer:
    reuse_addr = True
    max_queue_size = 5
    max_recv_size = 8192

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def server_bind(self):
        self.server.bind((self.host,self.port))
        if self.reuse_addr:
            self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def server_listen(self):
        self.server.listen(self.max_queue_size)

    def server_accept(self):
        self.conn, self.caddr = self.server.accept()
        self.verify_account()

    def verify_account(self):
        login_header = self.conn.recv(4)
        login_size = struct.unpack('i', login_header)[0]
        login_dict = self.conn.recv(login_size)
        username = login_dict['username']
        password = login_dict['password']
        login.UserBehavior.login(username, password)

    def get(self):
        pass

    def put(self):
        pass

    def run(self):
        self.server_bind()
        self.server_listen()
        self.server_accept()
        while True:
            print('服务端准备就绪，等待连接...')

            while True:
                cmd = self.conn.recv(self.max_recv_size)
                if not cmd:
                    print('客户端关闭，重置连接')
                    break
                request_method = cmd.decode('utf-8')[0]
                if hasattr(request_method):
                    func = getattr(self,request_method)
                    func()

if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8080)
    f.run()




