import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8083))

while True:
    cmd = input('>>>:')
    if not cmd:
        continue
    phone.send(cmd.encode('GBK'))
    data = phone.recv(1024)
    print(data.decode('GBK'))

phone.close()