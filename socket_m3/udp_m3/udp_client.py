import socket

phone  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ('127.0.0.1',8082)

while True:
    msg = input('>>>:')
    if not msg:
        continue
    phone.sendto(msg.encode('GBK'),ip_port)
    data = phone.recv(1024)
    print(data.decode('GBK'))