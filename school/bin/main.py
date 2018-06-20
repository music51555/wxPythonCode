import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import teacher,group,course,school

class ChoiceModules:

    def welcome(self):
        menu = {
            '1':t.set_teacher,
            '2':t.get_teacher,
            '3':t.del_teacher,
            '4':g.set_group,
            '5':g.get_group,
            '6':g.del_group,
            '7':c.set_course,
            '8':c.get_course,
            '9':c.del_course,
            '10':s.set_school,
            '11':s.get_school,
            '12':s.del_school
        }

        while True:
            print('1、 创建老师\n2、 获取老师列表\n3、 删除老师\n'
                  '4、 创建班级\n5、 获取班级列表\n6、 删除班级\n'
                  '7、 创建课程\n8、 获取课程列表\n9、 删除课程\n'
                  '10、创建学校\n11、获取学校列表\n12、删除学校\n')

            menu_num = input('请输入功能序号>>>:')

            if menu_num in menu.keys():
                func = menu[menu_num]

                if menu_num in ['1','3']:
                    teacher_name = input('请输入老师姓名，用逗号分割：')
                    teacher_list = teacher_name.split(',' or '，')
                    func(teacher_list)
                elif menu_num in ['4','6']:
                    group_name = input('请输入班级名称，用逗号分隔：')
                    group_list = group_name.split(',' or '，')
                    func(group_list)
                elif menu_num in ['7','9']:
                    course_name = input('请输入课程名称，用逗号分隔：')
                    course_list = course_name.split(',' or '，')
                    func(course_list)
                elif menu_num in ['10','12']:
                    school_name = input('请输入学校名称，用逗号分隔：')
                    school_list = school_name.split(',' or '，')
                    func(school_list)
                else:
                    func()

            else:
                print('您输入的功能序号不存在，请重新输入')
                continue

if __name__ == '__main__':
    w = ChoiceModules()
    t = teacher.Teacher()
    g = group.Group()
    c = course.Course()
    s = school.School()
    w.welcome()
