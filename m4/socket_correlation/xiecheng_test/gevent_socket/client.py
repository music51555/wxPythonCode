import socket,time
from threading import Thread,current_thread

def set_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8080))

    while True:
        msg = input('%s is say hello\n'%(current_thread().getName()))
        client.send(msg.encode('utf-8'))
        data = client.recv(1024)
        print(data.decode('utf-8'))

if __name__ == '__main__':
    start_time = time.time()
    for i in range(500):
        t = Thread(target=set_client)
        t.start()
    t.join()
    end_time = time.time()
    print(end_time - start_time)