class Foo:
    school = '北大青鸟'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('is talking')

f = Foo('alex',15)
print(hasattr(f,'name'))

print(getattr(f,'name1',None))

setattr(f,'name','peiqi')
print(f.__dict__)

delattr(f,'name')
print(f.__dict__)

class Student:

    school = '北大青鸟'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print('is studying')

    def talk(self):
        print('is talking')

s = Student('alex',15)

msg = input('>>>:')
if hasattr(s,msg):
    if callable(getattr(s,msg)):
        func = getattr(s,msg)
        func()
    else:
        print(getattr(s,msg))