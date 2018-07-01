**服务端**

UDP（user datagram protocol，用户数据报协议）是无连接的，面向消息的 ，udp协议是一对多的模式，服务端启动后，可以接收多个客户端的消息，并通过sendto指定ip的模式返回数据

```python
#服务端
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#设定服务端的IP和端口后，不用调用listen()和accept()端口，因为实现逻辑是客户端指定IP+端口后抛出消息，对应服务端接收到，同样通过指定IP+端口的形式将信息返回给客户端
phone.bind(('127.0.0.1',8082))

while True:
    #通过recvfrom方法接收消息，得到传输数据和客户端的IP+端口
    msg,addr = phone.recvfrom(1024)
    #当时用udp查询ipconfig命令返回结果时，会提示：
    #OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。因为udp协议认为一次send就是一个整体消息，是以消息为整体提取的
    obj = subprocess.Popen(msg.decode('GBK'),shell = True,
                     stdout = subprocess.PIPE,
                     stderr = subprocess.PIPE)
    stdout = obj.stdout.read()
    stderr = obj.stderr.read()
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
    #tcp是基于数据流的，于是收发的消息不能为空，这就需要在客户端和服务端都添加空消息的处理机制，防止程序卡住，而udp是基于数据报的，即便是你输入的是空内容（直接回车），那也不是空消息，包含了接收数据的IP、端口
    if not msg:
        continue
    #2、直接调用sendto方法（内容+IP和端口）
    phone.sendto(msg.encode('GBK'),ip_port)
    data = phone.recv(1024)
    print(data.decode('GBK'))
```

