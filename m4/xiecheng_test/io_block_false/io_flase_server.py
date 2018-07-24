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