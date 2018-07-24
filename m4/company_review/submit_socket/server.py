import socket
from concurrent.futures import ThreadPoolExecutor

def msg(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data.upper())

def sever_conn(ip,port):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((ip,port))
    server.listen(5)
    while True:
        conn,caddr = server.accept()
        pool.submit(msg, conn)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    sever_conn('127.0.0.1', 8080)
