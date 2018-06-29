class Mymeta(type):
    def __new__(cls, class_name,class_bases,class_dict):
        for k,v in class_dict.items():
            if k == 'school':
                k = k.upper()
                del class_dict['school']
                class_dict[k] = v
        return type.__new__(cls,class_name,class_bases,class_dict)

    def __init__(self,class_name,class_bases,class_dict):
        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

class Foo(metaclass = Mymeta):
    school = '北大青鸟'

    def talk(self):
        print('is talking')

print(Foo.__dict__)