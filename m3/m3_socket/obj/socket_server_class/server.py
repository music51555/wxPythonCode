import socket
import struct
import json
import os

class MyTCPServer:
    #AF_INET目的是使用ipv4通信，因为IPv4使用32位地址，相比IPv6的128位来说，计算更快，便于用于局域网通信
    address_family = socket.AF_INET

    #socket的流式协议
    socket_type = socket.SOCK_STREAM

    reuser_address = False
    #TCP发送缓存区和接收缓存区,默认是8192
    max_recv_size = 8192

    max_queue_size = 5

    share_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'share')

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket(self.address_family,
                                    self.socket_type)

    def server_bind(self):
        self.socket.bind((self.host,self.port))
        if self.reuser_address:
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server_address = self.socket.getsockname()
        print(self.server_address)

    def server_accept(self):
        return self.socket.accept()

    def server_listen(self):
        self.socket.listen(self.max_queue_size)

    def get_file_size(self,file_name):
        return os.path.getsize('%s/%s' % (self.share_dir, file_name))

    def get(self,conn,file_name):
        if os.path.exists('%s/%s' % (self.share_dir, file_name)):
            file_size = self.get_file_size(file_name)
        else:
            print('文件不存在，无法下载')
            return

        header_dict = {
            'file_name':file_name,
            'file_size':file_size
        }
        header_json = json.dumps(header_dict)
        header_bytes = header_json.encode('utf-8')
        conn.send(struct.pack('i',len(header_bytes)))
        conn.send(header_bytes)

        with open('%s/%s'%(self.share_dir,file_name),'rb') as f:
            for line in f:
                self.conn.send(line)

    def put(self,conn,file_name):
        if os.path.exists('%s/%s'%(self.share_dir, file_name)):
            print('文件已存在，无需重复上传')
            return
        header = conn.recv(4)
        header_size = struct.unpack('i',header)[0]
        header_bytes = conn.recv(header_size)
        header_dict = json.loads(header_bytes)

        file_size = header_dict['file_size']

        recv_size = 0
        with open('%s/%s'%(self.share_dir,file_name),'wb') as f:
            while recv_size < file_size:
                data = self.conn.recv(self.max_queue_size)
                f.write(data)
                recv_size += len(data)
                print('接收数据%s，文件总大小%s'%(recv_size,file_size))

    def run(self):
        while True:
            print('服务端启动...')
            self.conn,self.caddr = self.server_accept()
            while True:
                cmd = self.conn.recv(self.max_queue_size)
                if not cmd:
                    continue

                request_method = cmd.decode('utf-8').split()[0]
                file_name = cmd.decode('utf-8').split()[1]

                if hasattr(self,request_method):
                    func = getattr(self,request_method)
                    func(self.conn,file_name)
                else:
                    print('输入的命令有误，请重新输入')

if __name__ == '__main__':
    s = MyTCPServer('127.0.0.1',8081)
    s.server_bind()
    s.server_listen()
    s.run()
