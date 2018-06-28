import socket
import subprocess

phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

phone.bind(('127.0.0.1',8082))

while True:
    msg,addr = phone.recvfrom(1024)
    obj = subprocess.Popen(msg.decode('GBK'),shell = True,
                     stdout = subprocess.PIPE,
                     stderr = subprocess.PIPE)
    stdout = obj.stdout.read()
    stderr = obj.stderr.read()

    phone.sendto(stdout+stderr,addr)

phone.close()