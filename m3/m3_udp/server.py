from socket import *

server = socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',8080))

while True:
    #b'hello' ('127.0.0.1', 50432)
    data,caddr = server.recvfrom(1024)
    print(data,caddr)
    server.sendto(data.upper(),caddr)
