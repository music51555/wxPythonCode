import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8080))

phone.listen(5)

print('接收消息')
conn,caddr = phone.accept()
print(conn)
print(caddr)

data = conn.recv(1024)
print(data)

conn.send(data.upper())