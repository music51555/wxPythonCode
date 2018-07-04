class Mymeta(type):
    __instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance == None:
            obj = object.__new__(self)
            self.__init__(obj,*args,**kwargs)
            self.__instance = obj
            return obj
        return self.__instance

class Foo(metaclass = Mymeta):

    def __init__(self,name,age):
        self.name = name
        self.age = age

f1 = Foo('alex',12)
f2 = Foo('peiqi',12)
print(id(f1))
print(id(f2))