import socket_m3

phone = socket_m3.socket(socket_m3.AF_INET, socket_m3.SOCK_STREAM)

phone.connect(('127.0.0.1',8080))

while True:
    msg = input('>>>:')
    if not msg:
        continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data)