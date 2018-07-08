import configparser
import os
import sys


sys.path.append(os.path.dirname(__file__))
import set_md5

class set_Init():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    account_file = '%s/%s/account.init' % (base_dir, 'db')

    conf = configparser.ConfigParser()

    def set_conf(self,set_info,set_type,set_file):
        print(set_info)
        print(set_type)
        print(set_file)
        if 'username' in set_info.keys():
            username = set_info['username']
        if 'password' in set_info.keys():
            password = set_info['password']
            password_md5 = set_md5.set_md5(password)
        if 'file_name' in set_info.keys():
            file_name = set_info['file_name']

        # if set_type == 'set_account':
        #     print('进来了？')
        #     self.conf.read(set_file, encoding = 'utf-8')
        #     self.conf.add_section(username)
        #     self.conf.set(username, 'password', password_md5)
        #     self.conf.set(username, 'name', set_info['name'])
        #     self.conf.set(username, 'disk_size', str(set_info['disk_size']))
        #     self.conf.write(open(set_file, 'w',encoding = 'utf-8'))
        #     return

        if set_type == 'read_account':
            self.conf.read(set_file,encoding = 'utf-8')
            if self.conf.has_section(username) and password_md5 == self.conf.get(username,'password'):
                self.conf.clear()
                return True, username
            else:
                return False, username

        if set_type == 'set_recv_size':
            self.conf.read(set_file, encoding='utf-8')

            if not self.conf.has_section(file_name):
                self.conf.add_section(file_name)
                self.conf.set(file_name,'recv_size',str(set_info['recv_size']))
                with open(set_file,'w',encoding = 'utf-8') as f:
                    self.conf.write(f)
                return

s = set_Init()
ok,username = s.set_conf({'username': 'alex', 'password': '123456'},
           'read_account',
           '/Users/wangxin/Documents/wxPythonCode/wxPythonCode/m3/FTP_homework/db/account.init')

print('11111111111',ok,username)

s.set_conf({'file_name': '/Users/wangxin/Documents/wxPythonCode/wxPythonCode/m3/FTP_homework/share/alex/小猫钓鱼.mp4', 'recv_size': 1784},
           'set_recv_size',
           '/Users/wangxin/Documents/wxPythonCode/wxPythonCode/m3/FTP_homework/db/pause.init')
