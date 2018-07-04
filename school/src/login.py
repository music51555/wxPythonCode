import pickle,os,time,re

from src import register
from config import opration_file,hello
f = opration_file.Opration_file()
h = hello.Hello()

class Login:
    login_status = False

    def login(self):
        r = register.Register()

        def inner(func):
            while True:
                register_status = input('还没有账号？输入r开始注册账号,已有账号请按g>>>:')

                if register_status in ['r','R','g','G']:
                    if register_status in ['r', 'R']:
                        r.register()

                        user_info = f.read_file('../config/userinfo.pkl', 'rb')
                        print('账号注册成功，请登录')

                        while True:
                            username = input('请输入用户名：')
                            if username in user_info.keys():
                                password = input('请输入密码：')

                                if username == user_info[username]['username'] and password == user_info[username]['password']:
                                    print('登录成功')
                                    h.hello(user_info[username]['name'])
                                    Login.login_status = True
                                    func.welcome(user_info[username]['role'],user_info[username]['name'])
                                else:
                                    print('密码验证错误，请重新输入')
                                    continue

                            else:
                                print('您输入的用户名不存在，请重新输入')
                                continue

                    if register_status in ['g','G']:
                        if not os.path.exists('../config/userinfo.pkl'):
                            print('当前系统没有任何账号，请先注册')
                        else:
                            user_info = f.read_file('../config/userinfo.pkl', 'rb')

                            while True:
                                username = input('请输入用户名：')
                                if username in user_info.keys():
                                    password = input('请输入密码：')

                                    if username == user_info[username]['username'] and password == user_info[username]['password']:
                                        print('登录成功')
                                        h.hello(user_info[username]['name'])
                                        Login.login_status = True
                                        func.welcome(user_info[username]['role'],user_info[username]['name'])
                                    else:
                                        print('密码验证错误，请重新输入')
                                        continue

                                else:
                                    print('您输入的用户名不存在，请重新输入')
                                    continue

                else:
                    print('输入的序号有误，请重新输入')
                    continue

        return inner


