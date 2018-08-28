import socket
from threading import Thread

class Set_Server(Thread):
    def __init__(self):
        super(Set_Server,self).__init__()
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind(('127.0.0.1',8080))
        self.server.listen(5)

    def run(self):
        while True:
            print('starting')
            conn,caddr = self.server.accept()
            if conn:
                t = Thread(target=self.msg,args=(conn,))
                t.start()

    def msg(self,conn):
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(data.upper())
            except ConnectionResetError:
                break


if __name__ == '__main__':
    s = Set_Server()
    s.start()