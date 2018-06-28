import socket
import subprocess

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

phone.bind(('127.0.0.1',8083))

phone.listen(1)

while True:
    print('starting...')
    conn,caddr = phone.accept()
    print(caddr)
    print('获取连接客户端的IP地址和端口',conn.getpeername())


    while True:
        try:
            cmd = conn.recv(1024)
            obj = subprocess.Popen(cmd.decode('GBK'),shell = True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            print(len(stdout + stderr))

            conn.send(stdout + stderr)
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()

phone.close()

