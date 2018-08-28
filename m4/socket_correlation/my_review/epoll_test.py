import socket
import select

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)

epoll = select.epoll()
epoll.register(server.fileno(), select.EPOLLIN)


