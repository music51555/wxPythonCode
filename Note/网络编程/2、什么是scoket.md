##### 一、什么是scoket

网络编程，又被称为套接字（socket），在应用层和传输层中间添加了socket抽象层，实现客户端和服务端的通信。实际上socket是封装了传输层的TCP/IP协议，提供一组接口。来实现TCP/IP的数据传输，TCP（transport control protocol，传输控制协议）是面向连接的，面向流的，提供高可靠性服务 

##### 二、套接字类型：

**1、基于文件类型的套接字**：AF_UNIX

基于一台机器上的两个文件通信

**2、基于网络类型的套接字**：AF_INET

用于网络编程

##### 三、套接字的工作流程：

socket类，实例化套接字对象，调用接口

接口：

bind()：绑定IP

listen()：监听，客户端可以来链接了

connect()：连接服务器

accept()：接收链接

##### 四、实现套简单的接字通信

**服务端：**

```python
#服务端有两种套接字：
#1、phone，用于服务端接收建立连接
#2、conn，用于收发消息
import socket

#1、买手机，准备打电话
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#流式协议，TCP协议

#2、绑定手机卡（只有服务端需要绑定，客户端只要能联通服务端即可，无需绑定）
phone.bind(('127.0.0.1',8080))端口号是0-65535，0-1024是系统预留的端口

#3、开机（监听）
phone.listen(5)最大挂起的链接数

#4、等待接听电话，一旦接通电话就要有个结果，赋值给res，服务端的accept()接口和客户端的connect()接口对应，就是TCP协议的三次握手
print('starting...')
conn,client_addr = phone.accept() 
#客户端连接后执行，建立连接后，服务端拿到一个连接对象和客户端的地址，客户端拿到一个对象，通过这个对象可以进行收发消息
print(res)

#5、收发消息，收消息
data = conn.recv(1024) #接收数据的最大数，1、表示1024个字节，2、只接收1024个字节，即使是1025个字节
conn.send(data.upper())

#6、挂电话
conn.close()

#7、关机
phone.close()
```



**客户端：**

```python
#1、买手机
phone = socket.socket(socket.AF_INET,socket.scoket.SOCK_STREAM)

#2、拨号,套接字对象用于创建连接和首发消息
phone.connect(('127.0.0.1',8080))

#3、发、收消息
#因为服务端接收的bytes类型，字符串在内存中是unicode类型，所以需要编码为utf-8的二进制类型
phone.send('hello'.encode('utf-8'))
data = phone.recv(1024) 启动服务端后，先由客户端送消息，服务端接收后返回消息，客户端再接收消息
print(data)

#4、挂机
phone.close()
```

运行：

1、先启动服务端

2、再执行客户端