import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class School(resource.Resource):
    def get_school(self):
        super(School,self).get_resource('school')

    def set_school(self,school_name):
        super(School,self).set_resource(school_name,'school')

    def del_school(self,school_name):
        super(School,self).del_resource(school_name,'school')