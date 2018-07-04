import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Register(resource.Resource):
    def register(self):
        while True:
            print('1、学生账号\n2、老师账号\n3、管理账号')
            account_type = input('请选择您要创建的账号类型>>>:')
            if account_type in ['1', '2', '3']:

                if os.path.exists('../config/userinfo.pkl'):

                    user_info = f.read_file('../config/userinfo.pkl', 'rb')
                    while True:
                        username = input('请输入注册账号：')
                        for i in user_info:

                            if username in user_info[i].keys():
                                print('输入的账号已存在，请更换账号注册')
                                continue
                            else:
                                password = input('请输入注册密码：')
                                name = input('请输入姓名：')

                                user_info = f.read_file('../config/userinfo.pkl', 'rb')
                                super(Register,self).register(account_type,user_info,username,password,name)
                                return
                else:
                    while True:
                        username = input('请输入注册账号：')
                        password = input('请输入注册密码：')
                        name = input('请输入姓名：')

                        user_info = {}
                        super(Register,self).register(account_type, user_info, username, password, name)
                        return
            else:
                print('序号输入错误，请重新输入')
                continue






