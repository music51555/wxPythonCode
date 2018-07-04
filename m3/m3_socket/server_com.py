import socket
import subprocess
import struct

ip_port = ('127.0.0.1',8090)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ip_port)

server.listen(5)

while True:
    conn,caddr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024)
            obj = subprocess.Popen(cmd.decode('GBK'),
                             shell = True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            total_size = len(stdout) + len(stderr)

            header = struct.pack('i',total_size)
            conn.send(header)
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError as e:
            print(e)
            break

