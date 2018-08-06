from concurrent.futures import ThreadPoolExecutor
import socket

def conn_data(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data.upper())

def server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8081))
    server.listen(5)
    while True:
        conn,caddr = server.accept()
        executor.submit(conn_data,conn)

if __name__ == '__main__':
    executor = ThreadPoolExecutor(2)
    server()