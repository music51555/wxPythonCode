import pickle

from config import opration_file

f = opration_file.Opration_file()

class Resource:
    def pickle_file(self,resource_info,filename):
        resource_pkl = f.write_file(filename, 'wb')
        pickle.dump(resource_info, resource_pkl)

    def add_resource(self,resource_key,resource_name,resource,filename):
        resource_info = f.read_file(filename, 'rb')
        resource_info[resource_key][resource].append(resource_name)
        self.pickle_file(resource_info,filename)
        return

    def set_teacher(self,teacher_info,teacher_name,teacher_age,teacher_sex,teacher_school,filename):
        teacher_info[teacher_name] = {'age': teacher_age, 'sex': teacher_sex, 'group': [], 'school': teacher_school}
        self.pickle_file(teacher_info,filename)


    def set_course(self,course_info,sch,course_name,course_school,course_period,course_price,filename):
        course_info[course_name] = {'school': course_school, 'group': [], 'period': course_period,'price': course_price}
        sch.add_course(course_school, course_name)
        self.pickle_file(course_info,filename)
        return

    def set_group(self,group_info,sch,group_school,group_name,group_teacher,group_course,tea,filename):
        group_info[group_name] = {'school': group_school, 'teacher': group_teacher, 'course': group_course,'student': []}
        sch.add_group(group_name, group_school)
        tea.set_group(group_teacher, group_name)
        sch.course.set_group(group_course, group_name)
        self.pickle_file(group_info,filename)

    def set_school(self,school_info,school_name,school_address,filename):
        school_info[school_address] = {'name': school_name, 'address': school_address, 'course': [], 'teacher': [],'student': [], 'group': []}
        self.pickle_file(school_info,filename)
        return

    def set_student(self,student_info,student_name, student_age, student_sex,student_school,sch,filename):
        student_info[student_name] = {'age': student_age, 'sex': student_sex, 'school': student_school,'tuition': False}
        self.pickle_file(student_info,filename)
        sch.add_student(student_name, student_school)
        print('您已成功加入%s校区' % student_info[student_name]['school'])
        return

    def register(self,account_type,user_info,username,password,name):
        while True:
            print('请确认您的账号信息\n账号:%s\n密码:%s\n姓名:%s' % (username, password, name))
            confirm_account = input('确认请按y，重新输入请按n>>>')
            if confirm_account in ['y', 'Y', 'n', 'N']:
                if confirm_account in ['y', 'Y']:
                    if account_type == '1':
                        user_info[username] = {
                            'name': name, 'username': username, 'password': password,
                            'role': 'student'}
                    if account_type == '2':
                        user_info[username] = {
                            'name': name, 'username': username, 'password': password,
                            'role': 'teacher'}
                    if account_type == '3':
                        user_info[username] = {
                            'name': name, 'username': username, 'password': password,
                            'role': 'administrator'}
                    userinfo_pkl = f.write_file('../config/userinfo.pkl', 'wb')
                    pickle.dump(user_info, userinfo_pkl)
                    return
                if confirm_account in ['n', 'N']:
                    break
            else:
                print('您的输入有误，请重新输入')
                continue




