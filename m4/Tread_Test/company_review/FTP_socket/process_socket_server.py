import socket
from multiprocessing import Process

class FTPServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def set_server(self):
        self.server.bind(('127.0.0.1',8080))
        self.server.listen(5)
        while True:
            conn,caddr = self.server.accept()
            if conn:
                p = Process(target = self.server_recv,args = (conn,))
                p.start()
                continue

    def server_recv(self,conn):
        while True:
            data = conn.recv(1024)
            conn.send(data.upper())

if __name__ == '__main__':
    m = FTPServer()
    m.set_server()
