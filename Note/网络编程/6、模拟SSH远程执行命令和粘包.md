借助于subprocess模块，来模拟SSH远程执行命令

服务端

```python
import socket
import subproces

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

while True:
    print('starting')
    conn,caddr = phone.accept()

    while True:
        cmd = conn.recv(1024)
         if not cmd:
            break
        #客户端以什么样的编码发送命令，就以什么样的编码解码命令，windows时使用GBK编码
        obj = subprocess.Popen(cmd.decode('utf-8'),shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
        #读取命令的执行结果，命令的结果就是bytes类型，所以可以直接使用send方法发送
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
       
		#stdout和stderr是通过+号连接起来的，实际上是重新创建内存空间，导致效率低
        conn.send(stdout+stderr)

    conn.close()

phone.close()
```

客户端

```python
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8081))

while True:
    #粘包：就是在客户端没有接收完上次的结果，导致两次结果粘到了一起。当发送的命令是ls /时，返回的结果就会很少，在接收设置的1024个字节范围之内，但是当输入ifconfig后，接收的内容达到2826个，完全超出了1024个字节，所以第一次接收时只会输出1024个字节，导致在服务端到客户端发送信息的管道中积压的发送的数据，在IO缓冲区中积压了剩下的1082个字节，再次执行ls /命令时，命令的执行结果继续积压在了管道中，此时接收的是1082个字节中的1024个字节内容，仍是执行ifconfig命令残留的结果，这种现象被称为粘包现象，接收的是上一次残留的结果
    cmd = input('>>>:')
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))
    #接收命令的返回结果时，1024是个坑
    data = phone.recv(1024)
    #将接收的bytes类型的命令结果解码为系统识别编码
    print(data.decode('utf-8'))

phone.close()
```

send方法是把应用程序产生您的数据发送给操作系统的内存，拷贝给操作系统后就算完成了send操作，只有一步操作copy data

recv方法时等待接收数据，服务器操作系统通过网卡接口接收到数据，应用程序通过操作系统的内存拷贝数据到应用程序

**粘包的产生：**
1、时间间隔小，2、数据量小的包合并在一起发送，减少网络IO，此时产生了粘包

客户端：

```python
import socket
import time

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8081))
#1、客户端发送数据量小，时间间隔短时会产生粘包，是Nagle优化算法
phone.send('hello'.encode('utf-8'))
phone.send('world'.encode('utf-8'))

#2、如果间隔5秒发送第二次消息，在服务端的第二次消息就会接收到world
phone.send('hello'.encode('utf-8'))
time.sleep(5)
phone.send('world'.encode('utf-8'))

phone.close()
```

服务端：

```python
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

print('starting')
conn,caddr = phone.accept()

#1、打印helloworld，产生了粘包
cmd1 = conn.recv(1024)
print(cmd1)

#2、服务端接收一次数据后，完整的接收了客户端发送的数据，此时管道中没有残留数据，并在第二次接收数据时接收到了world，没有产生粘包，那么就意味着完整接收数据后就不会产生粘包
cmd1 = conn.recv(1024)
#打印hello
print(cmd1)
cmd2 = conn.recv(1024)
#打印world
print(cmd2)

#1-3、如果第一次只接收一个bytes，那么在第二次接收时，就会接收到第一次的残留数据ello+world
#接收到h
cmd1 = conn.recv(1)
print(cmd1)
#接收到elloworld
cmd2 = conn.recv(1024)
print(cmd2)

conn.close()

phone.close()
```



**解决粘包：简单版**

```python
#服务端
import socket
import subprocess
import struct

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',8081))

server.listen(5)

while True:
    conn,addr = server.accept()

    while True:
        cmd = conn.recv(1024)
        if not cmd:
            break
        obj = subprocess.Popen(cmd.decode('utf-8'),
                         shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        total_size = len(stdout)+len(stderr)
        #1、制定固定长度的报头，通过struct模块的pack方法，将i（integer）参数的数据长度进行封装为bytes类型的报头
        header = struct.pack('i',total_size)
        #2、把报头固定长度发给客户端，header本身就是bytes类型，所以可以直接发送
        conn.send(header)

        conn.send(stdout)
        conn.send(stderr)
    conn.close()

server.close()
```



```python
#客户端
import socket
import struct

ip_port = ('127.0.0.1',8090)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ip_port)

while True:
    cmd = input('>>>:')
    if not cmd:
        continue

    client.send(cmd.encode('GBK'))
	#1、客户端接收报头，接收stuct对象，struct包存放的是服务端传送数据的报头，包中封装着命令结果的数据长度，是bytes类型，长度是4，所以在客户端先接收4个字节长度的包，并通过struct模块的unpack解析数据包，得到数据长度
    header = client.recv(4)
    #2、从报头中解析对真实数据的描述信息
    total_size = struct.unpack('i',header)[0]
	#接收的bytes类型的数据结果，所以需要和提供的bytes类型空字符串相结合
    recv_data = b''
    recv_size = 0
    #针对数据结果的实际长度，循环接收结果内容
    while recv_size < total_size:
        data = client.recv(1024)
        recv_data += data
        recv_size += len(recv_data)
        print(recv_size)
    #3、打印数据结果
    print(recv_data.decode('GBK'))
```

