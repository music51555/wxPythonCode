import os
import configparser

class UserBehavior:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    account_file = '%s/%s/account.init' % (base_dir, 'db')

    conf = configparser.ConfigParser()

    def register(self):
        while True:
            while True:
                username = input('请输入注册账号：')
                if os.path.exists(self.account_file):
                    self.conf.read(self.account_file)
                    if self.conf.has_section(username):
                        print('注册的账户已存在，请更换用户名')
                        continue
                if not username.strip():
                    print('用户名不能为空,请重新输入')
                    continue
                break

            while True:
                password = input('请输入注册密码：')
                if not password.strip():
                    print('密码不能为空,请重新输入')
                    continue
                break

            while True:
                name = input('请输入姓名：')
                if not name.strip():
                    print('姓名不能为空,请重新输入')
                    continue
                break

            print(f'请确认您的注册信息：\n'
                  f'账号：{username}\n'
                  f'密码：{password}\n'
                  f'姓名：{name}')

            account_confirm = input('确认请按y，重新注册请按n>>>:')
            if account_confirm in ['y', 'Y', 'n', 'N']:
                if account_confirm in ['y', 'Y']:
                    user_info = {
                        'username': username,
                        'password': password,
                        'name': name
                    }

                    self.set_account(user_info,'set')
                    print('注册成功')
                    self.set_home_dir(username)
                    return
                if account_confirm in ['n', 'N']:
                    continue

    def login(self,login_info):
        if os.path.exists('%s/%s/%s' % (self.base_dir, 'db', 'account.init')):
            return self.set_account(login_info,'read')

    def set_account(self,login_info,mode):
        username = login_info['username']
        password = login_info['password']

        self.conf.read(self.account_file)

        if mode == 'set':
            self.conf.add_section(username)
            self.conf.set(username,'password',password)
            self.conf.set(username,'name',login_info['name'])
            self.conf.write(open(self.account_file,'w'))

        if mode == 'read':
            if self.conf.has_section(username) and password == self.conf[username]['password']:
                return True
            else:
                return False

    def set_home_dir(self,username):
        os.mkdir('%s/%s/%s'%(self.base_dir,'share',username))






