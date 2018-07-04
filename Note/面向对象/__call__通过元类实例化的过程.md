```python
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dict):
        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

    #通过__init__方法创建好了Foo类名对象，但当执行Foo()时，也就是调用Foo对象时，会执行__call__方法
    def __call__(self, *args, **kwargs):
        #实例化的步骤：1、创建一个空对象
        obj = object.__new__(self)
        #2、为对象执行初始化，定制对象的独有属性，如果不初始化对象也能执行成功，但是没有了Foo对象的name和age属性，所以Foo()实例化的对象f，没有了name和age属性，print(f.name)就是提示没有name属性
        self.__init__(obj,*args,**kwargs)
        #3、返回一个对象，这个对象就是调用Foo()实例化得到的f
        return obj

class Foo(object,metaclass = Mymeta):
    school = '北大青鸟'

    def __init__(self,name,age):
        self.name = name
        self.age = age

f = Foo('alex',12)
print(f.name,f.age)
```

