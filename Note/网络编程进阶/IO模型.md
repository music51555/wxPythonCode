IO模型

套接字服务端需要等到的IO操作时：

send

应用程序将数据拷贝给操作系统，接下来发送数据的操作就交给操作系统、网卡、物理传输去操作了

accept和recv

其中recv操作时由客户端发送消息，服务端等待接收，分为2个阶段

1、等待数据：

客户端通过将数据发送给操作系统，由操作系统发送给网卡，通过物理层传输到另一台计算机，也是由网卡传输给操作系统的缓存，

2、拷贝数据：

由操作系统拷贝给服务端的应用程序



**阻塞IO模型：**

就在原地等待结果，不运行后面的程序。同时经历了拷贝和等待两个阶段，应用程序通过recvfrom方法等待操作系统发送数据，此时是等待阶段。如果客户端发送了数据，那么操作系统就会接收到，并将数据拷贝给服务端应用程序，此时是拷贝阶段。

最初实现socket套接字连接时，是通过accept()方法接收连接后，去接收数据，并没有解决IO阻塞问题

接下来是通过多线程实现，在server方法的线程内实现accept()，在其他方法中实现接收和发送数据，也并没有解决IO阻塞问题，而是创建连接和接收数据的函数互不影响，但问题是会随着客户端的无限增多会浪费服务端的内存，因为开启了更多的线程

接下来是通过线程池来控制开启线程的数量，但总是会随着需求来增加线程池的数量，应用于规模较小的情况下，只是控制了开启线程的数量



非阻塞IO模型：

应用程序发送消息给操作系统，等待接收数据，如果没有数据的话，操作系统会给recvfrom应用程序发送消息，告知没有数据，而此时应用程序不会在等地等待，而是去执行其他任务，过一段时间再去发送消息给操作系统，检查是否有数据，一直循环这个步骤，所以可以再这个wait阶段去做更多的事

```python
#服务端
import socket

def talk(conn):
    data = conn.recv(1024)
    conn.send(data.upper())

def set_server():
    connected_list = []
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    print('starting...')
    server.setblocking(False)
    while True:
        try:
            conn,caddr = server.accept()
            connected_list.append(conn)
            print(connected_list)
        except BlockingIOError:
            dis_conn_list = []
            ready_send_list = []
            finish_send_list = []
            #接收消息
            for conn in connected_list:
                try:
                    data = conn.recv(1024)
                    ready_send_list.append((conn,data.upper()))
                except BlockingIOError:
                    continue
                except ConnectionResetError:
                    #如果这个连接的客户端断开了，那么就应该把这个客户端的连接从已连接的列表中删除，但是当前处于正在循环已连接列表的过程中，所以无法改变这个列表的内容，所以新建一个列表，来放入失去连接的conn
                    dis_conn_list.append(conn)

            #发送消息
            for item in ready_send_list:
                conn = item[0]
                data = item[1]
                try:
                    conn.send(data)
                    #一旦send的代码抛出异常，那么就不会执行此句代码，所以只有发送成功后，才会添加到已发送列表
                    finish_send_list.append(conn)
                except BlockingIOError:
                    pass

            for item in finish_send_list:
                finish_send_list.remove(item)

            for conn in dis_conn_list:
                connected_list.remove(conn)

if __name__ == '__main__':
    set_server()
```



```python
#客户端
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>>:')
    if not msg:
        continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

client.close()
```



缺点：

1、在没有客户端连接时，去做了其他接收消息的其他操作，但是如果此时有客户端连接，在执行其他代码时，不会及时响应到新的连接

2、服务端没有了阻塞，一直处于就绪状态，导致CPU会更可能多的分配给这个程序资源，形成了一个死循环，会导致内存溢出