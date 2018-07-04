import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class School(resource.Resource):
    filename = '../db/school.pkl'

    def __init__(self):
        pass

    def add_course(self,course_school,course_name):
        super(School,self).add_resource(course_school,course_name,'course',School.filename)

    def add_group(self,group_name,group_school):
        super(School,self).add_resource(group_school,group_name,'group',School.filename)

    def add_student(self,student_name,school_address):
        super(School,self).add_resource(school_address,student_name,'student',School.filename)

    def set_school(self,school_name,school_address):
        if not os.path.exists(School.filename):
            school_info = {}
            super(School,self).set_school(school_info,school_name,school_address,School.filename)
        else:
            school_info = f.read_file(School.filename, 'rb')
            if school_name in school_info.keys():
                print('该校区学校已存在，不能重复创建')
            super(School,self).set_school(school_info,school_name,school_address,School.filename)