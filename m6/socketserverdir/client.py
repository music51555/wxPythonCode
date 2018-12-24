import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while 1:
    data=input('>>>')
    client.send(data.encode('utf-8'))
    new_data=client.recv(1024)
    print(new_data.decode('utf-8'))