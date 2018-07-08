import socket
import sys
import os
import json
import struct

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import login
from core import pause
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
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            self.server.bind((self.host,self.port))
        except OSError:
            print('客户端关闭，服务端重置连接')
            return

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

    @property
    def get_free_size(self):
        disk_size = conf_obj.get_size(self.username)
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
        return free_size

    def file_diff(self,put_file_dict,puted_file):
        puted_file_md5 = set_md5.set_file_md5(puted_file)
        if puted_file_md5 == put_file_dict['file_md5']:
            put_status_dict = {
                'put_status': False,
                'put_message': '您的云空间中已存在该文件',
                'put_again':'no'
            }
            set_struct.struct_pack(self.conn, put_status_dict)
            return None
        else:
            put_status_dict  = {
                'put_status':False,
                'put_message':'云盘系统发现同名文件',
                'put_again':'yes'
            }
            set_struct.struct_pack(self.conn, put_status_dict)

            diff_dict = set_struct.struct_unpack(self.conn)
            f = diff_dict['file']
            file_name = diff_dict['file_name']
            recv_size = diff_dict['recv_size']
            return f,file_name,recv_size

    def size_not_enough(self,put_file_dict):
        put_status_dict = {
            'put_status': False,
            'put_message': '很抱歉，您的云盘空间不足，剩余空间为%sMB,您上传附件的大小是%sMB'
                           % (set_bytes.set_bytes(self.get_free_size),
                              set_bytes.set_bytes(put_file_dict['file_size'])),
            'put_again': 'no'
        }
        set_struct.struct_pack(put_status_dict)

    def get(self, filename):
        get_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,filename)
        pause_init = '%s/%s/%s' % (self.base_dir, 'db', 'pause.init')

        if os.path.exists(get_file):
            file_size = os.path.getsize(get_file)
            file_md5 = set_md5.set_file_md5(get_file)

            get_dict = {
                'file_name':filename,
                'file_size':file_size,
                'file_md5':file_md5,
                'get_status':True
            }
            set_struct.struct_pack(self.conn,get_dict)
            confirm_dict = set_struct.struct_unpack(self.conn)

            f = set_file.read_file(get_file, 'rb')
            if os.path.exists(pause_init):
                recv_size = conf_obj.set_conf({'file_name': get_file}, 'read_recv_size', pause_init)
                if 'is_pause_go' in confirm_dict.keys():
                    if confirm_dict['is_pause_go'] in ['y','Y']:
                        f.seek(int(recv_size))

            if confirm_dict['confirm_get'] == True:
                try:
                    for line in f:
                        self.conn.send(line)
                    print('下载任务完成')
                except BrokenPipeError as e:
                    print('客户端接收数据连接中断，服务端重置连接')
                    self.conn.close()
                    self.server_accept()
                    return
            else:
                return
        else:
            get_dict = {
                'get_status':False
            }
            set_struct.struct_pack(self.conn,get_dict)

    def put(self,filename):
        put_file_dict = set_struct.struct_unpack(self.conn)
        puted_file = '%s/%s/%s/%s'%(self.base_dir,'share',self.username,filename)
        pause_init = '%s/%s/%s' % (self.base_dir, 'db', 'pause.init')

        recv_size = 0
        recv_rate = 0

        if os.path.exists(puted_file):
            f,file_name,recv_size = self.file_diff(put_file_dict,puted_file)
            if not puted_file:
                return
        else:
            f = set_file.write_file(puted_file, 'wb')

        if put_file_dict['file_size'] < self.get_free_size:
            put_status_dict = {
                'put_status': True,
                'put_message': '请稍等,文件上传中...',
                'put_again':'no'
            }
            set_struct.struct_pack(self.conn, put_status_dict)

            while recv_size < put_file_dict['file_size']:
                data = self.conn.recv(self.max_recv_size)
                if not data:
                    pause_obj.set_pause(puted_file,recv_size,conf_obj,warnmsg = True)
                f.write(data)
                recv_size += len(data)

            get_file_md5 = set_md5.set_file_md5(puted_file)
            if get_file_md5 == put_file_dict['file_md5']:
                print('文件下载完成，校验MD5一致')
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

        if len(share_file_list) == 0:
            set_struct.struct_pack(self.conn, share_file_list)
        else:
            for file in share_file_list:
                view_dict[file] = {
                    'file_name':file,
                    'file_size':os.path.getsize('%s/%s/%s/%s'%(self.base_dir,'share',username,file)),
                    'put_date':set_time.set_time(os.path.getctime('%s/%s/%s/%s'%(self.base_dir,'share',username,file)))
                }
            set_struct.struct_pack(self.conn,view_dict)

    def run(self):
        while True:
            self.server_bind()
            self.server_listen()
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
    pause_obj = pause.Pause()
    conf_obj = set_init.set_Init()
    f.run()




