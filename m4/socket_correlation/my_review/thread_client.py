import socket

class Set_Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1',8080))

    def task(self):
        while True:
            msg = input('>>>:')
            if not msg:
                continue
            self.client.send(msg.encode('utf-8'))
            data = self.client.recv(1024)
            print(data.decode('utf-8'))

if __name__ == '__main__':
    s = Set_Client()
    s.task()