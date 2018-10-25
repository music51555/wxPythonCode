urls路由分发配置

##### 1、`urls.py`路由分发中使用正则表达式

```python
#在调用函数时，special_case_2003(request)，自动将request传入函数，只要正则表达式能匹配成功，即可访问
#re_path()是通过 from django.urls import path,re_path 引入的，表示路径支持正则表达式匹配
from django.urls import path,re_path

urlpatterns = [
    # ^articles/2003/$匹配以articles开头，以2003/结尾的路径，并调用special_case_2003(request)函数
    # 无需在路径前添加"/"，浏览器会自动在路径结尾添加"/"
    re_path(r'^articles/2003/$', views.special_case_2003),
]

#HttpResponse表示响应对象，填写响应格式中的响应体，不用写响应首行和响应头，因为Django的WSCI已经处理好了，HttpResponse的作用是传递一个字符串作为页面的内容
from django.shortcuts import render,HttpResponse

def special_case_2003(request):
    return HttpResponse('<h1>hello</h1>')

#路径匹配等价于
import re
re.search("^articles/2003/$","articles/2003/")
```



##### 2、`urls.py`路由分发中使用分组正则表达式

```python
#如果使用()分组正则表达式，分组所匹配的数据也会传入视图函数中，如year_chive(request,2003),所以在视图函数中也要对应的接收2个参数，year_chive(request,year)，而不像之前一样，只接收一个request参数
urlpatterns = [
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
]

#如果有多个分组，那么在视图函数中都要一一接收,所以要想传入参数，就使用正则表达式的分组
re_path(r'^articals/([0-9]{4})/([0-9]{2})$',year_archive)

def year_archive(request,year,month):
    return HttpResponse(year+'-'+month)

```



##### 3、有名分组

```python
# (?P<变量名>(正则表达式))来为分组取别名
urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_month_archive),
]

# 传入视图函数变为year_month_archiv(request,year=xxx,month=xxx)
def year_month_archive(request,year,month):
    return HttpResponse(year+'-'+month)
```



##### 4、以应用路径进行路由分发

```python
from django.urls import path,re_path,include

#首先在app01应用下新建urls.py作为自己应用下视图函数的路由分发
from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
    path('timer/', views.timer),
    path('login/', views.login),
    
    re_path(r'^articles/2003/$', views.special_case_2003),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_month_archive),
]

from django.urls import path,re_path,include

urlpatterns = [
    # 表示当在URL路径下遇到app01路径时，被分发到哪个应用下去继续路由分发，并根据app01后面的路径，去查找视图函数
    # 如http://127.0.0.1:8000/app01/articles/2003/，在路径中遇到app01/,通过项目的urls被分发到app01应用下的urls，通过路径去匹配视图函数
    re_path(r'app01/', include('app01.urls')),
    
    # 表示在路径下遇到任何开头时，后面路径被分发到aoo01.urls下去查找视图函数
    # 如http://127.0.0.1:8000/articles/2003/，直接被分发到app01应用下的urls
    re_path(r'^',include('app01.urls')),
]
```

