import socket
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread

def set_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))
    while True:
        client.send(('%s hello'%current_thread().getName()).encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(500)
    for i in range(500):
        pool.submit(set_client)
