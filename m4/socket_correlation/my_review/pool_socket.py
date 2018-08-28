#服务端，通过线程池启动线程，来实现限制启动的线程数，并通过异步提交的方式实现并行执行线程
from concurrent.futures import ThreadPoolExecutor
import socket

def task(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data.upper())

def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    pool = ThreadPoolExecutor(2)

    while True:
        conn,caddr = server.accept()
        pool.submit(task,conn)

if __name__ == '__main__':
    server()