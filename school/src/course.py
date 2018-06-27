import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Course(resource.Resource):
    filename = '../db/course.pkl'
    def set_group(self,group_course,group_name):
        super(Course,self).add_resource(group_course,group_name,'group',Course.filename)
        return

    def set_course(self,sch,course_school,course_name,course_period,course_price):
        if os.path.exists(Course.filename):
            course_info = f.read_file(Course.filename, 'rb')
            super(Course,self).set_course(course_info,sch,course_name,course_school,course_period,course_price,Course.filename)
        else:
            course_info = {}
            super(Course,self).set_course(course_info,sch,course_name,course_school,course_period,course_price,Course.filename)

