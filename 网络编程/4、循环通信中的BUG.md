##### 1、 客户端发送数据为空的BUG

##### 服务端

```python
#服务端
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

print('starting')
#conn是TCP协议三次握手产生的成果
conn,caddr = phone.accept()

while True:
    data = conn.recv(1024)
    print('接收客户端的数据',data)
    conn.send(data.upper())

conn.close()

phone.close()
```
##### 客户端
```python
#客户端
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8081))

while True:
    msg = input('>>>:')
    #当客户端直接成功的发送回车时，服务端并没有返回数据，导致客户端也卡在了接收消息代码处，所以从根本上解决使客户端不允许发送回车的问题。原因：应用程序产生数据是调用计算机的网卡去发送数据的，但是应用程序是无法操作系统硬件的，所以把要传输的数据拷贝给操作系统，由操作系统调用网卡来发送数据，但是应用系统产生的是一个空的回车数据，系统就会认为什么也没有拷贝到操作系统，就是空，所以不会调用网卡来发送数据，导致服务端也不会接收到数据，更不会发送回数据给客户端，客户端也不会接收到数据，导致程序卡主，根本原因就是系统就收到的是一个空数据
    if not msg:
        continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data)

phone.close()
```

应用程序产生的数据通过send产生数据，拷贝给操作系统，应用软件是操作应用层的，而操作系统是操作传输层、网络层、数据链层和物理层完成的数据传输，之所以调用TCP/IP协议，是因为在类的开头指定了socket.STREAM

##### 2、当客户端断开连接时

```python
#服务端
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

print('starting')
conn,caddr = phone.accept()

while True:
    data = conn.recv(1024)
    #在linux系统中，当客户端断开连接时，服务端会一直打印'接收客户端的数据'，是因为服务端一直在等待接收数据,所以添加如下代码，表示如果没有数据，就会执行break结束循环
    if not data:
        break
    print('接收客户端的数据',data)
    conn.send(data.upper())

conn.close()

phone.close()

#服务端
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

print('starting')
conn,caddr = phone.accept()

while True:
    #在windows系统下，不会一直等待接收数据，但是会报错ConnectionResetError，所以捕获异常后，执行break操作
    try:
        data = conn.recv(1024)
        print('接收客户端的数据',data)
        conn.send(data.upper())
    except ConnectionResetError:
        break

conn.close()

phone.close()
```
