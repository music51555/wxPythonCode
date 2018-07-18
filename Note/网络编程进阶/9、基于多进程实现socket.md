```python
#2、进程之间的内存空间是共享的还是隔离的？下述代码的执行结果是什么？

from multiprocessing import Process
n=100

def work():
    global n
    n=0
    print('子进程内: ',n)

#主进程和子进程在内存中是隔离的
if name == 'main':
    p=Process(target=work)
    p.start()
    print('主进程内: ',n)

'''
主进程得到n = 100
子进程得到n = 0
'''
```



```python
#3、基于多进程实现并发套接字
#服务端
import socket
from multiprocessing import Process

def talk(conn):
    while True:
        data = conn.recv(1024)
        conn.send(data.upper())

def server():
    print('starting...')
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
	#然后循环接收客户端的连接，接收到连接后创建进程，执行接收消息的函数，但是没开启几个进程，就会耗费服务端的内存，客户端的连接是无限的，会导致服务端内存崩溃
    while True:
        conn,caddr = server.accept()
        p = Process(target = talk,args = (conn,))
        p.start()

#先执行server函数，创建socket服务端连接
if __name__ == '__main__':
    server()
```

```python
#客户端，可以启动多个客户端，来发送命令到服务端，实现了多个客户端发送请求
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>>:')
    if not msg:
        continue
    client.send(msg.encode('UTF-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))
```

