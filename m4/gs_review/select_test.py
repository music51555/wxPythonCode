import socket
import select

def set_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('127.0.0.1',8085))
    server.listen(5)
    server.setblocking(False)
    rlist = [server, ]
    wlist = []
    wdata = {}

    while True:
        rl,wl,xl = select.select(rlist,wlist,[],0.5)
        print('rl',rl)
        print('wl',wl)
        for sock in rl:
            if sock == server:
                conn,data = sock.accept()
                rlist.append(conn)
            else:
                try:
                    data = sock.recv(1024)
                    if not data:
                        sock.close()
                        rlist.remove(sock)
                        continue
                    wlist.append(sock)
                    wdata[sock] = data.upper()
                except ConnectionResetError:
                    sock.close()
                    rlist.remove(sock)

        for conn in wl:
            conn.send(wdata[conn])
            wlist.remove(conn)
            wdata.pop(conn)

if __name__ == '__main__':
    set_server()
