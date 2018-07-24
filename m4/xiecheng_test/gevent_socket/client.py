import socket
from threading import Thread,current_thread

def set_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))

    count = 0
    while True:
        msg = input('%s is say hello,count %s'%(current_thread().getName(),count))
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8')+'\n')

if __name__ == '__main__':
    for i in range(500):
        t = Thread(target=set_client)
        t.start()