import configparser
import os

from setting import set_md5

class set_Init():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    account_file = '%s/%s/account.init' % (base_dir, 'db')

    conf = configparser.ConfigParser()

    def set_conf(self,set_info,set_type):
        self.conf.read(self.account_file)
        username = set_info['username']
        password = set_info['password']

        password_md5 = set_md5.set_md5(password)
        print(password_md5)

        if set_type == 'set':
            self.conf.add_section(username)
            self.conf.set(username, 'password', password_md5)
            self.conf.set(username, 'name', set_info['name'])
            self.conf.set(username, 'disk_size', str(set_info['disk_size']))
            self.conf.write(open(self.account_file, 'w'))

        if set_type == 'read':
            if self.conf.has_section(username) and password_md5 == self.conf[username]['password']:
                return True, username
            else:
                return False

    def get_size(self,username):
        self.conf.read(self.account_file)
        return self.conf[username]['disk_size']