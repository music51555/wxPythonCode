import os

from setting import set_file

class Pause():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pause_init = '%s/%s/%s' % (base_dir, 'db', 'pause.init')
    is_pause_go = ''

    def set_pause(self,file_name,recv_size,conf_obj,warnmsg):
        pause_dict = {
            'file_name': file_name,
            'recv_size': recv_size,
        }
        conf_obj.set_conf(pause_dict, 'set_recv_size', self.pause_init)
        if warnmsg == True:
            if file_name.find('share') != -1:
                print('客户端失去连接，重新启动服务端后，请重启客户端')
            if file_name.find('download') != -1:
                print('服务端失去连接，重新启动服务后，请再次启动客户端')
                exit()

    def read_pause(self,file_name,is_pause_go,terminal):
        if terminal == 'client':
            if is_pause_go in ['y', 'Y']:
                f = set_file.write_file(file_name, 'ab')
            if is_pause_go in ['n', 'N']:
                os.remove(file_name)
                f = set_file.write_file(file_name, 'wb')
        if terminal == 'server':
            if self.is_pause_go in ['y', 'Y']:
                f = set_file.read_file(file_name, 'rb')
            if self.is_pause_go in ['n', 'N']:
                f = set_file.read_file(file_name, 'rb')
                recv_size = 0
            else:
                f = set_file.write_file(file_name+'.diff', 'wb')
                recv_size = 0
        return f, file_name


