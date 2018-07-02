import socket
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from core import login
from setting import set_struct

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
        while True:
            login_info = set_struct.struct_unpack(self.conn)
            if login_info == None:
                break

            issuccess = login_obj.login(login_info)

            set_struct.struct_pack(self.conn, issuccess)
            if issuccess == True:
                print('账户验证成功，服务端准备就绪...')
                return
            else:
                print('账户验证失败，服务端重置连接...')
                continue

    def get(self):
        pass

    def put(self):
        pass

    def run(self):
        self.server_bind()
        self.server_listen()
        while True:
            self.server_accept()
            while True:
                try:
                    cmd = self.conn.recv(self.max_recv_size)
                    # if not cmd:
                    #     print('客户端关闭，服务端重置连接')
                    #     break
                    request_method = cmd.decode('utf-8')[0]
                    if hasattr(request_method):
                        func = getattr(self, request_method)
                        func()
                    self.conn.close()
                except ConnectionResetError as e:
                    print(e)
                    break


if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8080)
    print('请先登录...')
    login_obj = login.UserBehavior()
    f.run()




