import configparser
import os

from setting import set_md5

class set_Init():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    account_file = '%s/%s/account.init' % (base_dir, 'db')
    conf = configparser.ConfigParser()

    def set_conf(self,set_info,set_type,set_file):
        if 'username' in set_info.keys():
            username = set_info['username']
        if 'password' in set_info.keys():
            password = set_info['password']
            password_md5 = set_md5.set_md5(password)
        if 'file_name' in set_info.keys():
            file_name = set_info['file_name']

        if set_type == 'set_account':
            self.conf.read(set_file, encoding = 'utf-8')
            self.conf.add_section(username)
            self.conf.set(username, 'password', password_md5)
            self.conf.set(username, 'name', set_info['name'])
            self.conf.set(username, 'disk_size', str(set_info['disk_size']))
            self.conf.write(open(set_file, 'w',encoding = 'utf-8'))

        if set_type == 'read_account':
            self.conf.read(set_file,encoding = 'utf-8')
            if self.conf.has_section(username) and password_md5 == self.conf[username]['password']:
                self.conf.remove_section(username)
                return True, username
            else:
                self.conf.remove_section(username)
                return False, username

        if set_type == 'set_recv_size':
            self.conf.read(set_file,encoding = 'utf-8')
            if self.conf.has_section(file_name) == False:
                self.conf.add_section(file_name)
                self.conf.set(file_name,'recv_size',str(set_info['recv_size']))
                self.conf.write(open(set_file,'w',encoding = 'utf-8'))
            else:
                self.conf[file_name]['recv_size'] = str(set_info['recv_size'])
                self.conf.write(open(set_file, 'w',encoding = 'utf-8'))

        if set_type == 'read_recv_size':
            self.conf.read(set_file,encoding = 'utf-8')
            if self.conf.has_section(file_name):
                return self.conf[file_name]['recv_size']
            else:
                return None

    def get_size(self,username):
        self.conf.read(self.account_file)
        return self.conf[username]['disk_size']