epoll多路复用IO模型

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import select

# 创建socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置IP地址复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ip地址和端口号
server_address = ("127.0.0.1", 8888)
# 绑定IP地址
server.bind(server_address)
# 监听，并设置最大连接数
server.listen(10)
print("服务器启动成功，监听IP：", server_address)
# 服务端设置非阻塞
server.setblocking(False)
# 超时时间
timeout = 10
# 创建epoll事件对象，后续要监控的事件添加到其中
epoll = select.epoll()
# 注册要监控的文件句柄和事件
# 1、select.EPOLLIN表示可读事件，已连接状态
# 2、select.EPOLLOUT表示可写事件，准备发送消息状态
# 3、select.EPOLLERR表示错误事件
# 4、select.EPOLLHUP表示客户端断开事件，客户端失去连接的状态
epoll.register(server.fileno(), select.EPOLLIN)
# 保存连接客户端消息的字典，格式为{}
wdata = {}
# 文件句柄到所对应对象的字典，格式为{句柄：对象}
rlist_socket = {server.fileno(): server, }

while True:
    print("等待活动连接......")
    # 轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]，是一个列表
    # 当文件句柄发生变化，则会以列表的形式主动报告给用户进程,timeout为超时时间
    # 默认为-1，即一直等待直到文件句柄发生变化，如果指定为1
    # 那么epoll每1秒汇报一次当前文件句柄的变化情况，如果无变化则返回空
    events = epoll.poll(timeout)
    if not events:
        print("epoll超时无活动连接，重新轮询......")
        continue
    print("有", len(events), "个新事件，开始处理......")
    print('我要检查event:',events)
    for fd, event in events:
        socket = rlist_socket[fd]
        # 如果活动socket为服务端的socket，则去通过accept接收客户端的链接
        if socket == server:
            conn, caddr = server.accept()
            print("新连接：", caddr)
            # 新连接socket设置为非阻塞
            conn.setblocking(False)
            # 注册新连接fd到待读事件集合
            epoll.register(conn.fileno(), select.EPOLLIN)
            # 把新连接的文件句柄以及对象保存到字典
            rlist_socket[conn.fileno()] = conn
        # 关闭事件
        elif event & select.EPOLLHUP:
            print('client close')
            # 在epoll中注销客户端的文件句柄
            epoll.unregister(fd)
            # 关闭客户端的文件句柄
            rlist_socket[fd].close()
            # 在字典中删除与已关闭客户端相关的信息
            del rlist_socket[fd]
        # 可读事件
        elif event & select.EPOLLIN:
            # 接收数据
            data = socket.recv(1024)
            if data:
                print("收到数据：", data, "客户端：", socket.getpeername())
                # 将数据放入对应客户端的字典
                wdata[socket]=data
                print('检查wdata',wdata)
                # 修改读取到消息的连接到等待写事件集合(即对应客户端收到消息后，再将其fd修改并加入写事件集合)
                epoll.modify(fd, select.EPOLLOUT)
        # 可写事件
        elif event & select.EPOLLOUT:
                # 从字典中获取对应客户端的信息
                data = wdata[socket]
                print("发送数据：", data, "客户端：", socket.getpeername())
                # 发送数据
                socket.send(data)
                wdata.pop(socket)
                epoll.modify(fd, select.EPOLLIN)

# 在epoll中注销服务端文件句柄
# epoll.unregister(server.fileno())
# 关闭epoll
epoll.close()
# 关闭服务器socket
server.close()
```



#思路：

#设置服务端的socket

#创建epoll对象，epoll = select.epoll()

#通过服务端socket对象的句柄fileno()，将服务端的socket注册为监听事件

epoll.register(server.fileno(),select.EPOLLIN)

#和select方式一样，将已连接的服务端和客户端socket都添加至rdict中，格式为{句柄：socket}

rdit_socket = {server.fileno():server,}

#同时也创建wdata = {}，来存储客户端发送的消息

#通过events = epoll.poll()来轮询socket是否有事件

#循环for fd,event in events，因为socket都已经被添加至rdict_socket字典，key为fileno()，所以判断if rdict_socket(fd) == server，则去通过accept()连接客户端

#并将客户端的socket通过epoll.register()注册，epoll.register(conn.fileno(),select.EPOLLIN)，表示将客户端注册为准备接收类型的EPOLL

#继续判断如果event & select.EPOLLIN那么就通过socket = rdict_socket(fd)，data = socket.recv(1024)去接收消息

#接收消息后将接收的data，以socket为key存储在wdata字典中，并通过socket的fd注册为EPOLLOUT

epoll.modify(fd,EPOLLOUT)表示准备发送消息

#继续判断如果event & select.EPOLLOUT，data = wdata[socket]，socket.send(data)就可以发送消息了，发送消息后将已发送的消息删除，wdata.pop(socket)，并将类型设置为select.EPOLLIN，表示准备接收下一次的消息，epoll.modify(fd,select.EPOLLIN)

#继续判断，如果event & select.EPOLLHUP，表示客户端断开了连接，则将socket关闭，并在rdict中删除，rdict_socket[fd].close()，rdict_socket.pop(fd)，最重要的是通过unregister方法取消监听该socket，epoll.unregister(fd)



```python
import socket
import select

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_address = ('127.0.0.1',8080)
server.bind(server_address)
server.listen(5)
server.setblocking(False)
print('服务端启动成功，监听IP：',server_address)

epoll = select.epoll()
epoll.register(server.fileno(),select.EPOLLIN)

rdict_socket = {server.fileno():server,}
wdata = {}

while True:
    print('等待客户端连接...')
    #event返回的是一个列表，列表里面存的是一个一个元组，元组存储socket的fileno句柄，和触发的事件id
    events = epoll.poll(10)
    if not events:
        print('没有客户端连接，服务端重新监听')
        continue
    print('有',len(events),'新的事件，开始处理...')
    for fd,event in events:
        socket = rdict_socket[fd]
        if socket == server:
            conn,caddr = server.accept()
            print('客户端地址是：',caddr)
            rdict_socket[conn.fileno()] = conn
            epoll.register(conn.fileno(),select.EPOLLIN)
        elif event & select.EPOLLIN:
            data = socket.recv(1024)
            if data:
                print('收到消息',data)
                wdata[socket] = data
                epoll.modify(fd,select.EPOLLOUT)
        elif event & select.EPOLLOUT:
            data = wdata[socket]
            if data:
                socket.send(data.upper())
                wdata.pop(socket)
                epoll.modify(fd,select.EPOLLIN)
        elif event & select.EPOLLHUP:
            socket.close()
            rdict_socket.pop(fd)
            epoll.unregister(fd)

epoll.close()
server.close()
```

