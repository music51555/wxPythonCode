import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8080))

phone.listen(5)

print('准备接收客户端连接')
conn,caddr = phone.accept()

while True:
    try:
        data = conn.recv(1024)
        conn.send(data.upper())
    except ConnectionResetError as e:
        print(e)
        break
