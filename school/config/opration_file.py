import pickle

class Opration_file:
    def read_file(self,filename,mode):
        if mode == 'r':
            f = open(filename,'r',encoding = 'utf-8')
            return f
        elif mode == 'rb':
            f = open(filename,'rb')
            resource_info = pickle.load(f)
            return resource_info

    def write_file(self,filename,mode):
        if mode == 'w':
            f = open(filename,'w',encoding = 'utf-8')
            return f
        elif mode == 'wb':
            f = open(filename,'wb')
            return f
        elif mode == 'ab':
            f = open(filename,'ab')
            return f