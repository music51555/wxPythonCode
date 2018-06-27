import socket_m3

phone = socket_m3.socket(socket_m3.AF_INET, socket_m3.SOCK_STREAM)
phone.setsockopt(socket_m3.SOL_SOCKET, socket_m3.SO_REUSEADDR, 1)

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
