web应用程序的请求发送过程

发送请求是借助浏览器客户端，作为client，发送请求到服务端，请求过程

服务器中一定有server.py来运行程序，服务器接收到请求后返回数据，响应过程

```python
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
    # 如果此时通过浏览器访问该地址，会显示127.0.0.1发送的响应无效，说明服务端已经接收到了客户端发送的数据，但是数据响应无效
    conn.send(b'hello world')
    # 如果与web进程通信，则必须按照http协议格式发送数据，固定格式
    # HTTP1.1 200 OK为响应首行
    # hello world为响应体，是浏览器要加载的内容
    conn.send(b'HTTP1.1 200 OK\r\n\r\nhello world')
    conn.close()
```



**preview**：从服务端接收的返回数据

![Preview](.\images\Preview.png)

**response**：浏览器加载的数据

![Response](.\images\Response.png)



服务器返回**读取的html文件**

```python
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
    with open(temples,'r',encoding='utf-8') as f:
        fdata = f.read()
        print(fdata)
    conn.send(('HTTP1.1 200 OK\r\n\r\n%s'%fdata).encode('utf-8'))
    conn.close()
```



服务器返回**rb模式读取的文件**

```python
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
    with open(temples,'rb') as f:
        fdata = f.read()
        print(fdata)
    conn.send((b'HTTP1.1 200 OK\r\n\r\n')+fdata)
    conn.close()
```

