import gevent
import socket
from gevent import monkey;monkey.patch_all()

def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('127.0.0.1',8080))
    s.listen(5)
    while True:
        conn,caddr = s.accept()
        gevent.spawn(task,conn)

def task(conn):
    data = conn.recv(1024)
    conn.send(data.upper())

if __name__ == '__main__':
    g1 = gevent.spawn(server)
    g1.join()