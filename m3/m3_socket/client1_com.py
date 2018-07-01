import socket
import struct

ip_port = ('127.0.0.1',8090)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ip_port)

while True:
    cmd = input('>>>:')
    if not cmd:
        continue

    client.send(cmd.encode('GBK'))

    header = client.recv(4)
    total_size = struct.unpack('i',header)[0]

    recv_data = b''
    recv_size = 0
    while recv_size < total_size:
        print('come in')
        data = client.recv(1024)
        recv_data += data
        recv_size += len(recv_data)
        print(recv_size)
    print(recv_data.decode('GBK'))