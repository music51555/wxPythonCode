import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

phone.bind(('127.0.0.1',8082))

while True:
    msg,addr = phone.recvfrom(1024)
    phone.sendto(msg.upper(),addr)

phone.close()