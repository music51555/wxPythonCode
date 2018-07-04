```python
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dict):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
            
        if '__doc__' not in class_dict or not class_dict['__doc__'].strip():
            raise TypeError('必须添加注释，且注释不能为空')
            
        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

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
```
