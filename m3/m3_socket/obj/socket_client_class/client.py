import socket
import struct
import json
import os

class MyTCPClient:
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'download')

    socket_family = socket.AF_INET

    socket_type = socket.SOCK_STREAM

    max_recv_size = 8192

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.client = socket.socket(self.socket_family,self.socket_type)

    def server_connect(self):
        self.client.connect((self.host,self.port))

    def get_file_size(self,filename):
        return os.path.getsize('%s/%s'%(self.download_dir,filename))

    def put(self,cmd,file_name):
        if os.path.exists('%s/%s' % (self.download_dir, file_name)):
            file_size = self.get_file_size(file_name)
            header_dict = {
                'cmd': cmd,
                'file_name': cmd.split()[1],
                'file_size': file_size
            }

            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode('utf-8')

            self.client.send(struct.pack('i', len(header_bytes)))
            self.client.send(header_bytes)

            with open('%s/%s' % (self.download_dir, file_name),'rb') as f:
                for line in f:
                    self.client.send(line)
        else:
            print('文件不存在,请重新输入')

    def get(self,cmd,file_name):
        if os.path.exists('%s/%s' % (self.download_dir, file_name)):
            print('文件已存在，无需重复下载')
            return

        header = self.client.recv(4)
        header_size = struct.unpack('i',header)[0]
        header_bytes = self.client.recv(header_size)
        header_dict = json.loads(header_bytes)
        file_size = header_dict['file_size']

        recv_size = 0
        with open('%s/%s'%(self.download_dir,file_name),'wb') as f:
            while recv_size < file_size:
                data = self.client.recv(self.max_recv_size)
                f.write(data)
                recv_size += len(data)
                print('接收数据%s，文件总大小%s'%(recv_size,file_size))


    def run(self):
        while True:
            cmd = input('>>>:')
            if not cmd:
                continue
            file_name = cmd.split()[1]
            self.client.send(cmd.encode('utf-8'))

            if hasattr(self,cmd.split()[0]):
                func = getattr(self,cmd.split()[0])
                func(cmd,file_name)

if __name__ == '__main__':
    c = MyTCPClient('127.0.0.1',8081)
    c.server_connect()
    c.run()

