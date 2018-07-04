from socket import *

client = socket(AF_INET,SOCK_DGRAM)

while True:
    cmd = input('>>>:')
    client.sendall(cmd.encode('utf-8'),('127.0.0.1',8080))
    data,server_addr = client.recvfrom(1024)
    print(data,server_addr)