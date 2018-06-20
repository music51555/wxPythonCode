import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Student(resource.Resource):
    def get_student(self):
        super(Student,self).get_resource('student')

    def set_student(self,student_name):
        super(Student,self).set_resource(student_name,'student')

    def del_student(self,student_name):
        super(Student,self).del_resource(student_name,'student')