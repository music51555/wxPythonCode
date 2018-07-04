import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Group(resource.Resource):
    filename = '../db/group.pkl'

    def get_student(self,group_list):
        group_info = f.read_file('../db/group.pkl', 'rb')

        while True:
            for i, v in enumerate(group_list):
                print(str(i + 1) + '、' + v)

            group_num = input('请选择要查看的班级序号：')
            if group_num.isdigit():
                group_num = int(group_num)
                if group_num in list(range(len(group_list) + 1))[1:]:
                    if len(group_info[group_list[(group_num - 1)]]['student']) > 0:
                        print(','.join(group_info[group_list[(group_num - 1)]]['student']))
                        return
                    else:
                        print('您管理的班级，还没有学生选择，等待已认证的同学加入吧')
                        return
                else:
                    print('序号输入错误，请重新输入')
                    continue
            else:
                print('序号输入错误，请重新输入')
                continue


    def get_group(self,name):
        if os.path.exists('../db/group.pkl'):
            group_info = f.read_file('../db/group.pkl', 'rb')

            data_list = []
            for i in group_info:
                if group_info[i]['school'] == name:
                    data_list.append(i)

                if group_info[i]['course'] == name:
                    data_list.append(i)
            return data_list

        else:
            print('抱歉，%s校区还没有开设任何班级，如需开通请联系管理员。'%name)
            return None

    def set_group(self,sch,group_school,group_name,group_teacher,group_course,tea):
        if os.path.exists(Group.filename):
            group_info = f.read_file(Group.filename, 'rb')
            super(Group,self).set_group(group_info,sch,group_school,group_name,group_teacher,group_course,tea,Group.filename)
        else:
            group_info = {}
            super(Group,self).set_group(group_info,sch,group_school,group_name,group_teacher,group_course,tea,Group.filename)


