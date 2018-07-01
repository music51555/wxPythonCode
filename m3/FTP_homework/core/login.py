import os
import json
import configparser

from setting import set_file

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UserBehavior:
    print('请先登录...')

    account_file = '%s/%s/account.init' % (base_dir, 'db')
    write_file = set_file.write_file(account_file, 'w')

    def register(self):
        username = input('请输入注册账号：')
        password = input('请输入注册密码：')
        name = input('请输入姓名：')

        self.set_account(username,password)
        print('注册成功')
        return

    def set_account(self,username,password):
        read_file = set_file.read_file(self.account_file, 'r')
        conf = configparser.ConfigParser()
        conf.read(self.account_file)

        conf.add_section(username)
        conf.set(username,'password',password)

        conf.write(self.write_file)

    def login(self,username,password):
        if os.path.exists('%s/%s/%s' % (base_dir, 'core', 'account.init')):
            read_file = set_file.read_file(self.account_file, 'r')
            user_info = json.load(read_file)
            while True:
                if username in user_info.keys() and password == user_info[username]['password']:
                    print('登录成功')
                    return
                else:
                    print('您输入的用户名或密码错误，请重新输入')
                    continue
        else:
            print('当前系统还没有任何账号，请先注册')
            return


