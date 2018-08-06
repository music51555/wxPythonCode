import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Student(resource.Resource):
    filename = '../db/student.pkl'
    def set_student(self,student_name, student_age, student_sex,student_school,sch):
        if os.path.exists('../db/student.pkl'):
            student_info = f.read_file('../db/student.pkl', 'rb')
            if student_name in student_info.keys():
                print('您已是%s校区的学生'%student_info[student_name]['school'])
                return
            else:
                super(Student,self).set_student(student_info,student_name, student_age, student_sex,student_school,sch,Student.filename)
        else:
            student_info = {}
            super(Student, self).set_student(student_info, student_name, student_age, student_sex, student_school,sch,Student.filename)

    def set_stu_group(self,student_name,student_group):
        group_info = f.read_file('../db/group.pkl', 'rb')

        if student_name in group_info[student_group]['student']:
            print('您已经是%s班级的学员'%student_group)
        else:
            group_info[student_group]['student'].append(student_name)
            group_pkl = f.write_file('../db/group.pkl', 'wb')

            pickle.dump(group_info, group_pkl)
            print('您已成功加入%s班级' % student_group)
            return

    def pay_tuition(self,name):
        if os.path.exists('../db/student.pkl'):
            student_info = f.read_file('../db/student.pkl', 'rb')

            if name in student_info.keys() and student_info[name]['tuition'] == True:
                print('您已经缴纳过学费，无需重复缴纳')
                return

            if os.path.exists('../db/group.pkl'):
                group_info = f.read_file('../db/group.pkl', 'rb')

                for group in group_info:
                    if name in group_info[group]['student']:
                        course_info = f.read_file('../db/course.pkl', 'rb')

                        course = group_info[group]['course']
                        price = course_info[course]['price']
                        if group in course_info[course]['group']:
                            while True:
                                print('您所在的%s班级，开展的是%s课程，应缴纳学费%s元' % (group, course, price))
                                tuition = input('请输入您缴纳的学费：')

                                if not tuition.isdigit():
                                    print('学费信息输入错误，请重新输入')
                                else:
                                    if tuition == price:
                                        student_info[name]['tuition'] = True
                                        student_pkl = f.write_file('../db/student.pkl', 'wb')
                                        pickle.dump(student_info, student_pkl)
                                        print('感谢您的支持，努力加油学习吧！')
                                        return
                                    else:
                                        if int(tuition) < 0:
                                            print('学费信息输入错误，请重新输入')
                                            continue
                                        else:
                                            print('学费信息输入错误，请重新输入')
                                            continue
                        else:
                            continue

                    else:
                        print('您还没有选择班级哦，请先选择班级吧')
                        continue
            else:
                print('您所在的校区，还没有开设班级，请联系管理员创建班级')
                return

        else:
            print('请先认证学员')

    def student_auth(self,name,sch):
        while True:
            student_name = input('请输入学员姓名：')
            if student_name != name:
                print('您只能对自己的账号进行认证哦')
                continue

            if os.path.exists('../db/student.pkl'):
                student_info = f.read_file('../db/student.pkl', 'rb')

                if student_name in student_info.keys():
                    print('您已经认证过学员了，不能重复认证')
                    return

            student_age = input('请输入学员年龄：')
            student_sex = input('请输入学员性别：')
            while True:
                student_school = input('请输入所在校区:')
                if not os.path.exists('../db/school.pkl'):
                    print('抱歉，没有查询到任何学校信息，如需开通请联系管理员')
                    return
                else:
                    school_info = f.read_file('../db/school.pkl', 'rb')

                    if student_school not in school_info.keys():
                        print('抱歉，没有查询到%s地区开设的校区，如需开通请联系管理员'%student_school)
                        check_school = input('查询校址请按c>>>：')
                        if check_school == 'c':
                            for school in school_info:
                                print(school)
                                continue
                    else:
                        self.set_student(student_name, student_age, student_sex, student_school, sch)
                        return

    def select_group(self,sch):
        while True:
            if os.path.exists('../db/student.pkl'):
                student_name = input('请输入学员姓名:')

                student_info = f.read_file('../db/student.pkl', 'rb')

                if student_name not in student_info.keys():
                    print('您还不是学员，请先注册学员')
                else:
                    while True:
                        student_school = input('请输入所在校区:')
                        if not os.path.exists('../db/school.pkl'):
                            print('抱歉，未查询到任何学校信息，如需开通请联系管理员')
                            return
                        else:
                            school_info = f.read_file('../db/school.pkl', 'rb')

                            if student_school not in school_info.keys():
                                print('抱歉，%s还没有开设校区，如需开通请联系管理员' % student_school)
                                check_school = input('重新输入校区请按b，查询校区请按c>>>：')
                                if check_school == 'c':
                                    for school in school_info:
                                        print(school)
                                        continue
                                if check_school == 'b':
                                    continue
                            else:
                                group_list = sch.group.get_group(student_school)

                                if group_list == None:
                                    return
                                else:
                                    print('北京校区包含如下班级：')
                                    for group in group_list:
                                        print(group)
                                    while True:
                                        student_group = input('请输入你要加入的班级名称：')
                                        if student_group in group_list:
                                            self.set_stu_group(student_name, student_group)
                                            return
                                        else:
                                            print('班级不存在，请重新输入')
                                            continue
            else:
                print('请先认证学员')
                return