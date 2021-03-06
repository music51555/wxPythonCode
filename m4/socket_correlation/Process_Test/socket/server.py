import socket
from multiprocessing import Process

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

def task(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data.upper())

def set_server():
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    while True:
        conn,caddr = server.accept()

        p = Process(target = task,args = (conn,))
        p.start()

if __name__ == '__main__':
    set_server()

