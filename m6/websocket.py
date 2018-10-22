import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8800))
server.listen(5)

while 1:
    print('waiting')
    conn,caddr = server.accept()
    data = conn.recv(1024)
    print(data)
    # 添加html标签样式后，浏览器会渲染字符串中的标签样式
    with open('./html/index.html','r',encoding='utf-8') as f:
        fdata = f.read()
        print(fdata)
    conn.send(('HTTP1.1 200 OK\r\n\r\n%s'%fdata).encode('utf-8'))
    conn.close()