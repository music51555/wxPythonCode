import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Course(resource.Resource):
    def get_course(self):
        super(Course,self).get_resource('course')

    def set_course(self,course_name):
        super(Course,self).set_resource(course_name,'course')

    def del_course(self,course_name):
        super(Course,self).del_resource(course_name,'course')