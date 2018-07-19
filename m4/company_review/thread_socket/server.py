from threading import Thread
import socket

def conn():
    while True:


def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    conn,caddr = server.accept()
    t = Thread(target = conn,args = (conn,))
    t.start()