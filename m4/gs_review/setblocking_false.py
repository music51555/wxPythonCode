import socket

def set_Server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8080))
    server.listen(5)
    server.setblocking(False)
    connected_list = []
    ready_send_list = []
    while True:
        try:
            conn,caddr = server.accept()
            connected_list.append(conn)
        except:
            dis_connect_list = []
            for conn in connected_list:
                try:
                    data = conn.recv(1024)
                    if not data:
                        dis_connect_list.append(conn)
                    ready_send_list.append((conn,data.upper()))
                except BlockingIOError:
                    continue
                except ConnectionResetError:
                    dis_connect_list.append(conn)

            finish_send_list = []
            for item in ready_send_list:
                conn = item[0]
                data = item[1]
                conn.send(data)
                finish_send_list.append(item)

            for item in finish_send_list:
                ready_send_list.remove(item)

            for conn in dis_connect_list:
                connected_list.remove(conn)

if __name__ == '__main__':
    set_Server()