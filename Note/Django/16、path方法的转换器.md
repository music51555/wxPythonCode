Django2.0版本的path

在1.0的`re_path()`的用法与`url()`的用法是完全一样的，如果有分组正则表达式，那么在调用视图函数时，会传递给视图函数分组参数

```python
#在请求http://127.0.0.1:8000/articles/2003/index/路径时，在全局路由分发时通过匹配到了r'articles/([0-9]{4})'路径，调用views.index函数时会将分组传输传递给函数
re_path(r'articles/([0-9]{4})',views.index)

#所以添加一个形参year，来接收分组参数，打印参数的数据类型为字符串，如果需要进行计算，要进行数据类型转换
def index(request,year):
    print(year)
    print(type(year))
```



所以使用Django2.0的path方法的转换器

re_path：使用正则表达式

path：使用转换器

```python
#<int:>表示整型转换器，<int:year>是一个有名分组，将字符串转换成整型后传递，以后在匹配正整数时，直接使用int转换器，再次打印参数类型时，变为<class 'int'>
urlpatterns = [
    path('articles/<int:year>/',views.index)
    re_path('articles/([0-9]{4})',views.index)
]
```



转换器一共有5种：

```python
#匹配请求路径hello，http://127.0.0.1:8000/articles/hello/
path('articles/<str:year>/',views.index)
#匹配整型字符串，http://127.0.0.1:8000/articles/2003/
path('articles/<int:year>/',views.index)
#匹配字母、数字、横杠、下划线组成的字符串,http://127.0.0.1:8000/articles/2003_hello/
path('articles/<slug:year>/',views.index)
#匹配uuid，如 075194d3-6885-417e-a8a8-6c931e272f00。
path('articles/<uuid:year>/',views.index)
#匹配任何非空字符串,包含特殊字符，http://127.0.0.1:8000/articles/2003nihao_##/
path('articles/<path:year>/',views.index)
```



##### 自定义转换器

以上的5种转换器无法满足用户的需求，所以需要自定义转换器，converter  美 /kən'vɝtɚ/  转换器

```python
#创建Rex_Mons.py，存储自定义转换器类
class Mons:
    #属性必须为regex，存储正则表达式，也就是通过正则表达式匹配数据
    regex = '[0-9]{2}'

    #to_python函数名不允许改变
    def to_python(self,value):
        return int(value)
    
    #用于反向解析
    def to_url(self,value):
        return '%04d' % value
```



```python
#引入转换器函数register_converter
from django.urls import register_converter
from ... import Mons

#注册自定义的转换器类中的函数Mons，为转换器起别名
register_converter(Mons,"rm")

#在路由分发中调用转换器
urlpatterns = [
    path('articles/<rm:month>/',views.index),
]

#在视图函数中接收的形参名，要与转换器中的变量名匹配
def index(request,month):
    print(month)
    print(type(month))
    return HttpResponse('OK')
```

