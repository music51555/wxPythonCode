import os
import configparser

from setting import set_init
from setting import set_struct

class UserBehavior:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    account_file = '%s/%s/account.init' % (base_dir, 'db')

    conf = configparser.ConfigParser()
    init = set_init.set_Init()

    put_size_1mb = 1024000
    put_size_total_mb = put_size_1mb * 100

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
                        'name': name,
                        'disk_size':self.put_size_total_mb
                    }

                    self.init.set_conf(user_info,'set_account',self.account_file)
                    print('恭喜您，注册成功，您获得100MB云空间')
                    self.set_home_dir(username)
                    return
                if account_confirm in ['n', 'N']:
                    continue
            else:
                print('您的输入有误，请重新输入')
                continue

    def login(self,client):
        while True:
            login_choice = input('还没有账号？按r注册账号，已有账号请按g>>>：')
            if login_choice in ['r', 'R', 'g', 'G']:
                if login_choice in ['r', 'R']:
                    self.register()
                    continue

                if login_choice in ['g', 'G']:
                    if not os.path.exists('%s/%s/%s' % (self.base_dir, 'db', 'account.init')):
                        print('当前系统内还没有任何账号，请先注册')
                        continue

                    while True:
                       username = input('请输入用户名：')
                       password = input('请输入密码：')

                       login_info = {
                           'username': username,
                           'password': password
                       }

                       set_struct.struct_pack(client,login_info)
                       is_success_dict = set_struct.struct_unpack(client)

                       if is_success_dict['is_success'] == True:
                           self.username = is_success_dict['username']
                           print('登录成功')
                           return username
                       else:
                           print('用户名或密码错误，请重新输入')
                           continue
            else:
                print('您的输入有误，请重新输入')
                continue

    def verify_account(self,login_info):
        if os.path.exists('%s/%s/%s' % (self.base_dir, 'db', 'account.init')):
            return self.init.set_conf(login_info,'read_account',self.account_file)

    def set_home_dir(self,username):
        os.mkdir('%s/%s/%s'%(self.base_dir,'share',username))






