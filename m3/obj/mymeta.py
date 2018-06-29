class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dict):
        print(class_dict)
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        if '__doc__' not in class_dict or not class_dict['__doc__'].strip():
            raise TypeError('必须添加注释，且注释不能为空')
        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

    def __call__(self, *args, **kwargs):
        print('开始类的实例化')
        obj = object.__new__(self)
        #__call__方法是当调用实例化的对象时执行的方法，Mymeta类实例化的对象是Foo类
        #如果不初始化对象也能执行成功，但是没有了Foo对象的name和age属性，所以Foo()实例化的对象f，没有了name和age属性
        self.__init__(obj,*args,**kwargs)
        return obj

class Foo(object,metaclass = Mymeta):
    '''
    这是注释
    '''
    school = '北大青鸟'

    def __init__(self,name,age):
        self.name = name
        self.age = age

f = Foo('alex',12)
print(f.name,f.age)