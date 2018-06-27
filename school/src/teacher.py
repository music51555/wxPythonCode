import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Teacher(resource.Resource):
    filename = '../db/teacher.pkl'
    def set_teacher(self,teacher_name,teacher_age,teacher_sex,teacher_school):
        if os.path.exists(Teacher.filename):
            teacher_info = f.read_file(Teacher.filename,'rb')
            super(Teacher,self).set_teacher(teacher_info,teacher_name,teacher_age,teacher_sex,teacher_school,Teacher.filename)
        else:
            teacher_info = {}
            super(Teacher,self).set_teacher(teacher_info,teacher_name,teacher_age,teacher_sex,teacher_school,Teacher.filename)

    def set_group(self,teacher_name,group_name):
        super(Teacher,self).add_resource(teacher_name,group_name,'group',Teacher.filename)

    def get_group(self,teacher_name):
        if os.path.exists('../db/teacher.pkl'):
            teacher_info = f.read_file('../db/teacher.pkl', 'rb')

            if os.path.exists('../db/group.pkl'):
                print('您当前所管理的班级是：')
                group_list = teacher_info[teacher_name]['group']
                if len(teacher_info[teacher_name]['group']) == 0:
                    print('您还未管理任何班级，在创建班级时会由管理员指定讲师')
                    return None
                else:
                    print(','.join(teacher_info[teacher_name]['group']))
                    return group_list
            else:
                print('该校区没有任何班级，请联系管理员创建班级')
                return

        else:
            print('未查询到认证讲师，请先进行讲师认证操作')
            return

    def teacher_auth(self,name):
        while True:
            teacher_name = input('请输入老师姓名：')
            if teacher_name != name:
                print('您只能对自己的账号进行认证哦')
                continue

            if os.path.exists('../db/teacher.pkl'):
                teacher_info = f.read_file('../db/teacher.pkl', 'rb')

                if teacher_name in teacher_info.keys():
                    print('您已经认证过教师了，不能重复认证')
                    return
            else:
                teacher_age = input('请输入老师年龄：')
                while True:
                    sex = input('请输入老师性别：')
                    if sex in ['男', '女']:
                        teacher_sex = sex
                        break
                    else:
                        print('性别输入错误,请重新输入：')
                        continue

                while True:
                    teacher_school = input('请输入所在校区:')
                    if not os.path.exists('../db/school.pkl'):
                        print('抱歉，没有查询到任何学校信息，如需开通请联系管理员')
                        return
                    else:
                        school_info = f.read_file('../db/school.pkl', 'rb')

                        if teacher_school not in school_info.keys():
                            print('抱歉，没有查询到%s地区开设的校区，如需开通请联系管理员' % teacher_school)
                            check_school = input('重新输入校区请按b，查询校址请按c>>>：')

                            if check_school == 'c':
                                for school in school_info:
                                    print(school)
                                    continue

                            if check_school == 'b':
                                continue

                        else:
                            self.set_teacher(teacher_name, teacher_age, teacher_sex,teacher_school)
                            print('讲师认证成功')
                            return