import os,pickle

from config import opration_file
from src import resource

f = opration_file.Opration_file()

class Group(resource.Resource):
    def get_group(self):
        super(Group,self).get_resource('group')

    def set_group(self,group_name):
        super(Group,self).set_resource(group_name,'group')

    def del_group(self,group_name):
        super(Group,self).del_resource(group_name,'group')