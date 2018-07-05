import socket
import sys
import os
import json
import struct
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from core import login
from setting import set_struct
from setting import set_file
from setting import set_md5
from setting import set_init
from setting import set_bytes
from setting import set_time

class FTPServer:
    max_queue_size = 5
    max_recv_size = 8192
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.encoding = sys.getdefaultencoding()

    def server_bind(self):
        self.server.bind((self.host,self.port))
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    def server_listen(self):
        self.server.listen(self.max_queue_size)

    def server_accept(self):
        self.conn, self.caddr = self.server.accept()
        while True:
            login_info = set_struct.struct_unpack(self.conn)
            if login_info == None:
                break

            is_success,self.username = login_obj.login(login_info)
            is_success_dict = {
                'is_success':is_success,
                'username':self.username
            }

            set_struct.struct_pack(self.conn, is_success_dict)
            if is_success_dict['is_success'] == True:
                print('账户验证成功，服务端准备就绪...')
                return
            else:
                print('账户验证失败，服务端重置连接...')
                continue

    def get(self):
        pass

    @property
    def get_free_size(self):
        disk_size = init.get_size(self.username)
        share_file_list = os.listdir('%s/%s/%s' % (self.base_dir,
                                                   'share',
                                                   self.username))
        total_size = 0
        for file in share_file_list[1:]:
            total_size += os.path.getsize('%s/%s/%s/%s' % (self.base_dir,
                                                           'share',
                                                           self.username,
                                                           file))
        free_size = int(disk_size) - total_size
        print('free_size',free_size)
        return free_size

    def file_diff(self,put_file_dict,puted_file):
        puted_file_md5 = set_md5.set_file_md5(puted_file)
        print(puted_file_md5)
        print(put_file_dict['file_md5'])
        if puted_file_md5 == put_file_dict['file_md5']:
            put_status_dict = {
                'put_status': False,
                'put_message': '您的云空间中已存在该文件',
                'put_again':'no'
            }
            set_struct.struct_pack(self.conn, put_status_dict)
            return
        else:
            put_status_dict  = {
                'put_status':False,
                'put_message':'云盘系统发现同名文件，但文件内容较旧，是否继续上传？',
                'put_again':'yes'
            }
            set_struct.struct_pack(self.conn, put_status_dict)
            diff_dict = set_struct.struct_unpack(self.conn)
            print(diff_dict)
            while True:
                if diff_dict['set_diff'] in ['y', 'Y']:
                    os.remove(puted_file)
                    return
                if diff_dict['set_diff'] in ['n', 'N']:
                    puted_file = '%s/%s/%s/%s.diff' % (self.base_dir,
                                                       'share',
                                                       self.username,
                                                       put_file_dict['file_name'])
                    return puted_file

    def size_not_enough(self,put_file_dict):
        put_status_dict = {
            'put_status': False,
            'put_message': '很抱歉，您的云盘空间不足，剩余空间为%sMB,您上传附件的大小是%sMB'
                           % (set_bytes.set_bytes(self.get_free_size),
                              set_bytes.set_bytes(put_file_dict['file_size'])),
            'put_again': 'no'
        }
        header_json = json.dumps(put_status_dict)
        header_bytes = header_json.encode('utf-8')
        self.conn.send(struct.pack('i', len(header_bytes)))
        self.conn.send(header_bytes)


    def put(self,filename):
        put_file_dict = set_struct.struct_unpack(self.conn)
        puted_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,filename)
        recv_size = 0
        recv_rate = 0

        print('put_file_dict',put_file_dict)

        if os.path.exists(puted_file):
            puted_file = self.file_diff(put_file_dict,puted_file)

        if put_file_dict['file_size'] < self.get_free_size:
            put_status_dict = {
                'put_status': True,
                'put_message': '请稍等,文件上传中...',
                'put_again':'no'
            }
            set_struct.struct_pack(self.conn, put_status_dict)

            f = set_file.write_file(puted_file, 'wb')
            while recv_size < put_file_dict['file_size']:
                data = self.conn.recv(self.max_recv_size)
                f.write(data)
                recv_size += len(data)
                print('接收文件大小%s，文件总大小%s'%(recv_size,put_file_dict['file_size']))
            else:
                self.put_file_dict = put_file_dict
                print('服务端：文件上传完毕')
            return
        else:
            self.size_not_enough(put_file_dict)
        return

    def view(self,username):
        view_dict = {}
        share_file_list = os.listdir('%s/%s/%s'%(self.base_dir,
                                                 'share',
                                                 username))[:]
        print('hare_file_list'+repr(share_file_list))
        if len(share_file_list) == 0:
            set_struct.struct_pack(self.conn, share_file_list)
        else:
            for file in share_file_list:
                view_dict[file] = {
                    'file_name':file,
                    'file_size':os.path.getsize('%s/%s/%s/%s'%(self.base_dir,'share',username,file)),
                    'put_date':set_time.set_time(os.path.getctime('%s/%s/%s/%s'%(self.base_dir,'share',username,file)))
                }
            print(view_dict)
            set_struct.struct_pack(self.conn,view_dict)

    def run(self):
        self.server_bind()
        self.server_listen()
        while True:
            self.server_accept()
            while True:
                # try:
                cmd = self.conn.recv(self.max_recv_size)
                if not cmd:
                    print('客户端关闭，服务端重置连接')
                    break
                request_method = cmd.decode(self.encoding).split()[0]
                request_content = cmd.decode(self.encoding).split()[1]

                if hasattr(self,request_method):
                    func = getattr(self, request_method)
                    func(request_content)
                    continue
                self.conn.close()
                # except ConnectionResetError as e:
                #     print(e)
                #     break

if __name__ == '__main__':
    f = FTPServer('127.0.0.1',8082)
    print('请先登录...')
    login_obj = login.UserBehavior()
    init = set_init.set_Init()
    f.run()




