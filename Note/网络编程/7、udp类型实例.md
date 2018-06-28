**服务端**
```python
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#设定服务端的IP和端口后，不用调用listen()和accept()端口，因为实现逻辑是客户端指定IP+端口后抛出消息，对应服务端接收到，同样通过指定IP+端口的形式将信息返回给客户端
phone.bind(('127.0.0.1',8082))

while True:
    #通过recvfrom方法接收消息
    msg,addr = phone.recvfrom(1024)
    #必须使用sendto方法，send方法无法实现指定ip+端口的功能
    phone.sendto(msg.upper(),addr)

phone.close()
```



**客户端**

```python
import socket

#socket.SOCK_DGRAM表示udp类型
phone  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#1、不用像TCP协议一样需要事先连接服务端
ip_port = ('127.0.0.1',8082)

while True:
    msg = input('>>>:')
    if not msg:
        continue
    #2、直接调用sendto方法（内容+IP和端口）
    phone.sendto(msg.encode('GBK'),ip_port)
    data = phone.recv(1024)
    print(data.decode('GBK'))
```

