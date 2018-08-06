import socket
import select

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)

#存储套接字对象，一是建立连接的server,二是连接接收到的conn
rlist = [server,]
#存储待发送数据的套接字对象conn
wlist = []
#存储待发送的数据
wdata = {}

while True:
    #询问操作系统，是否接收到客户端的连接，select
    rl,wl,xl = select.select(rlist,wlist,[],0.5)
    print('rlist',rl)
    print('wlist',wl)
    for sock in rl:
        if sock == server:
            conn,caddr = sock.accept()
            rlist.append(conn)
        else:
            #windows系统当客户端断开连接时会报异常
            try:
                data = sock.recv(1024)
                #而linux系统会一直接口空的消息，所以关闭断开的连接，并将该连接移除
                if not data:
                    sock.close()
                    rlist.remove(sock)
                wlist.append(sock)
                wdata[sock] = data.upper()
            except ConnectionResetError:
                rlist.remove(sock)

    for sock in wl:
        data = wdata[sock]
        sock.send(data)
        wlist.remove(sock)
        wdata.pop(sock)


