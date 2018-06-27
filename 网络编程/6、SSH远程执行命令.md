借助于subprocess模块，来模拟SSH远程执行命令

服务端

```python
import socket
import subproces

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1',8081))

phone.listen(5)

while True:
    print('starting')
    conn,caddr = phone.accept()

    while True:
        cmd = conn.recv(1024)
        #客户端以什么样的编码发送命令，就以什么样的编码解码命令，windows时使用GBK编码
        obj = subprocess.Popen(cmd.decode('utf-8'),shell = True,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
        #读取命令的执行结果，命令的结果就是bytes类型，所以可以使用send方法发送
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        if not cmd:
            break
		#stdout和stderr是通过+号连接起来的，实际上是重新创建内存空间，导致效率低
        conn.send(stdout+stderr)

    conn.close()

phone.close()
```



客户端

```python
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1',8081))

while True:
    #当发送的命令是ls /时，返回的结果就会很少，在接收设置的1024个字节范围之内，但是当输入ifconfig后，接收的内容达到2826个，完全超出了1024个字节，所以第一次接收时只会输出1024个字节，导致在服务端到客户端发送信息的管道中积压的发送的数据，积压了剩下的1082个字节，再次执行ls /命令时，继续积压在了管道中，接收的实际上是残留1082个字节中的1024个字节，这种现象被称为粘包现象，接收的上一次残留的结果
    cmd = input('>>>:')
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))
    #接收命令的返回结果时，1024是个坑
    data = phone.recv(1024)
    #将接收的bytes类型的命令结果解码
    print(data.decode('utf-8'))

phone.close()
```

