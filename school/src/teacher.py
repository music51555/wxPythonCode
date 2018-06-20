import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Teacher(resource.Resource):
    def get_teacher(self):
        super(Teacher,self).get_resource('teacher')

    def set_teacher(self,teacher_name):
        super(Teacher,self).set_resource(teacher_name,'teacher')

    def del_teacher(self,teacher_name):
        super(Teacher,self).del_resource(teacher_name,'teacher')