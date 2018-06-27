import os,sys,pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import teacher,group,course,school,student,login,register,score

from config import opration_file
f = opration_file.Opration_file()

class Course_System:
    print('欢迎使用选课系统')

    @login.Login.login
    def __init__(self):
        pass

    def student_auth(self,name):
        stu.student_auth(name,sch)

    def select_group(self):
        stu.select_group(sch)

    def group_info(self,name):
        tea.get_group(name)

    def student_info(self,name):
        group_list = tea.get_group(name)
        if group_list == None:
            return

        sch.group.get_student(group_list)

    def teacher_auth(self,name):
        tea.teacher_auth(name)

    def creat_group(self):
        if not os.path.exists('../db/school.pkl'):
            print('请先创建学校')
            return
        if not os.path.exists('../db/course.pkl'):
            print('请先创建课程')
        else:
            while True:
                group_school = input('请输入所在校区：')
                school_info = f.read_file('../db/school.pkl', 'rb')
                if group_school not in school_info.keys():
                    print('抱歉，%s地区还没有开办学校，如需开通请联系管理员'%group_school)
                    while True:
                        check_school = input('查询校区请按c>>>：')
                        if check_school in ['c','C']:
                            print('目前在以下城市开办了学校：')
                            num = 1
                            for school in school_info:
                                print(str(num) + '、 ' + school)
                                num += 1
                            break
                        else:
                            print('您的输入有误，请重新输入')
                            continue
                else:
                    while True:
                        group_name = input('请输入班级名称,查询当前校区已开设的班级请按c>>>')
                        if group_name == 'c':
                            if len(school_info[group_school]['group']) == 0:
                                print('该校区还未开设任何班级')
                                continue
                            else:
                                for group in school_info[group_school]['group']:
                                    print(group)
                                continue
                        if not group_name:
                            print('您的输入有误，请重新输入')
                            continue
                        if group_name in school_info[group_school]['group']:
                            print('班级已存在，请重新输入')
                            continue
                        else:
                            while True:
                                group_teacher = input('请输入班级讲师：')
                                if not os.path.exists('../db/teacher.pkl'):
                                    print('没有查询到已认证的%s讲师，如需认证，请登录讲师账号后，在教师园地中认证老师' % group_teacher)
                                    return
                                else:
                                    teacher_info = f.read_file('../db/teacher.pkl', 'rb')
                                    if group_teacher not in teacher_info.keys():
                                        check_teacher = input('没有查询到已认证的%s讲师，查询认证讲师请按c>>>' % group_teacher)
                                        if check_teacher == 'c':
                                            for teacher in teacher_info:
                                                print(teacher)
                                            continue
                                    print('正在查询当前校区开设的课程...')
                                    if os.path.exists('../db/course.pkl'):
                                        course_info = f.read_file('../db/course.pkl', 'rb')

                                        num = 1
                                        course_dict = {}
                                        for course in course_info:
                                            if course_info[course]['school'] == group_school:
                                                course_dict[str(num)] = course
                                                num += 1
                                            else:
                                                print('%s校区还未开设任何课程，请先创建该校区的课程'%group_school)
                                                return

                                        while True:
                                            for i in course_dict:
                                                print(str(i) + '、 ' + course_dict[str(i)])
                                            group_course = input('请选择班级开展的课程的序号：')
                                            if group_course not in course_dict:
                                                print('您的输入有误，请重新输入')
                                                continue
                                            sch.group.set_group(sch, group_school,group_name, group_teacher,course_dict[group_course], tea)
                                            print('班级添加成功')
                                            return
                                    else:
                                        print('请先创建课程')
                                        return

    def creat_course(self):
        if not os.path.exists('../db/school.pkl'):
            print('请先创建学校')
            return
        while True:
            if os.path.exists('../db/school.pkl'):
                school_info = f.read_file('../db/school.pkl', 'rb')
                num = 1
                for school in school_info:
                    school_dict = {str(num):school}
                print('目前已开办的校区如下：')
                for key in school_dict:
                    print(key+'、 '+school_dict[key])
                choice_school = input('您要在哪所校区开展课程？请输入序号：')
                if choice_school in school_dict.keys():
                    while True:
                        course_name = input('请输入开展的课程名称：')
                        if not os.path.exists('../db/course.pkl'):
                            course_period = input('请输入课程开展的周期：')
                            course_price = input('请输入课程报名价格：')
                            sch.course.set_course(sch, school_dict[choice_school], course_name, course_period, course_price)
                            print('<%s校区成功添加%s课程>' % (school_dict[choice_school], course_name))
                            return
                        else:
                            course_info = f.read_file('../db/course.pkl', 'rb')
                            if course_name in course_info.keys() and school_dict[choice_school] == course_info[course_name]['school']:
                                print('该学校已经创建过该课程，请重新输入')
                                continue
                            else:
                                course_period = input('请输入课程开展的周期：')
                                course_price = input('请输入课程报名价格：')
                                sch.course.set_course(sch, school_dict[choice_school], course_name, course_period,course_price)
                                print('<%s校区成功添加%s课程>' % (school_dict[choice_school], course_name))
                                return
                else:
                    print('您的输入有误，请重新输入')
                    continue
            else:
                print('未查询到任何学校，请先创建学校')
                return

    def creat_school(self):
        school_name = input('请输入学校名称：')
        school_address = input('请输入学校校区：')
        sch.set_school(school_name,school_address)
        print('学校创建成功')

    def add_score(self,name):
        group_list = tea.get_group(name)
        if group_list == None:
            return

        sco.add_score(group_list)

    def edit_score(self,name):
        group_list = tea.get_group(name)
        if group_list == None:
            return

        sco.edit_score(group_list)

    def student_pay_tuition(self,name):
        stu.pay_tuition(name)

    menu = {
        '1' : student_auth,
        '2' : select_group,
        '3' : student_pay_tuition,
        '4' : teacher_auth,
        '5' : group_info,
        '6' : creat_school,
        '7' : creat_group,
        '8' : creat_course,
        '9' : student_info,
        '10': add_score,
        '11': edit_score
    }

    def welcome(self,role,name):
        while True:
            print('1、 学生园地\n2、 教师园地\n3、 系统管理')
            menu_num = input('欢迎使用选课系统，请选择功能序号>>>:')

            if menu_num in ['1','2','3']:
                if menu_num == '1':
                    if role != 'student':
                        print('只有学员账号才可以访问此模块')
                        continue

                    while True:
                        print('1、学员认证\n2、选择班级\n3、缴纳学费')
                        sub_menu_num = input('请选择功能序号,返回上级菜单请按b>>>:')
                        if sub_menu_num in ['b', 'B']:
                            break
                        if sub_menu_num in ['1', '2', '3']:
                            if sub_menu_num == '1':
                                func = Course_System.menu['1']
                                func(self,name)

                            if sub_menu_num == '2':
                                func = Course_System.menu['2']
                                func(self)

                            if sub_menu_num == '3':
                                func = Course_System.menu['3']
                                func(self,name)
                        else:
                            print('您输入的序号有误，请重新输入')
                            continue

                if menu_num == '2':
                    if role != 'teacher':
                        print('只有讲师账号才可以访问此模块')
                        continue

                    while True:
                        print('1、讲师认证\n2、查看班级\n3、查看学员\n4、学员打分\n5、修改成绩')
                        sub_menu_num = input('请选择功能序号，返回上级菜单请按b>>>:')
                        if sub_menu_num in ['b', 'B']:
                            break
                        if sub_menu_num in ['1', '2', '3','4', '5']:
                            if sub_menu_num == '1':
                                func = Course_System.menu['4']
                                func(self,name)

                            if sub_menu_num == '2':
                                func = Course_System.menu['5']
                                func(self,name)

                            if sub_menu_num == '3':
                                func = Course_System.menu['9']
                                func(self,name)

                            if sub_menu_num == '4':
                                func = Course_System.menu['10']
                                func(self,name)

                            if sub_menu_num == '5':
                                func = Course_System.menu['11']
                                func(self,name)
                        else:
                            print('您输入的序号有误，请重新输入')
                            continue

                if menu_num == '3':
                    if role != 'administrator':
                        print('只有管理员账号才可以访问此模块')
                        continue

                    while True:
                        print('1、创建学校\n2、创建班级\n3、创建课程')
                        sub_menu_num = input('请选择功能序号,返回上级菜单请按b>>>:')
                        if sub_menu_num in ['b', 'B']:
                            break

                        if sub_menu_num in ['1', '2', '3']:
                            if sub_menu_num == '1':
                                func = Course_System.menu['6']
                                func(self)

                            if sub_menu_num == '2':
                                func = Course_System.menu['7']
                                func(self)

                            if sub_menu_num == '3':
                                func = Course_System.menu['8']
                                func(self)
                        else:
                            print('您输入的序号有误，请重新输入')
                            continue
            else:
                print('您输入的序号有误，请重新输入')
                continue

if __name__ == '__main__':
    sch = school.School()
    sch.group = group.Group()
    sch.course = course.Course()
    stu = student.Student()
    tea = teacher.Teacher()
    sco = score.Score()
    course_system = Course_System()