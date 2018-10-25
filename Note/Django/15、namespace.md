namespace

主要解决问题是：

如果在应用的路由分发`urls.py`中有相同的别名，如`name='index'`，那么在视图函数中`reverse(别名)`的时候都会打印为一样的路径，所以在项目路由分发的时候，为每一个应用设置namespace，然后尽管应用的路由分发别名一样，但是在视图函数中通过`app01:index`和`app02:index`都会打印各自别名所对应的路径

在Django项目的`urls.py`文件根据应用名称进行路由分发

```python
urlpatterns = [
    re_path(r'app01/', include('app01.urls')),
    re_path(r'app02/', include('app02.urls')),
]
```

再到各自app01、app02应用下的`urls.py`中，根据应用后面的路径`index`匹配视图函数

```python
#app01的urls.py，路径别名都被命名为index，只有在urls.py中设置路径和视图函数时，才去设置别名
urlpatterns = [
    re_path('index/',views.index,name='index')
]
#app02的urls.py，路径别名都被命名为index
urlpatterns = [
    re_path('index/',views.index,name='index')
]
```

调用应用下`views.py`中的`index`函数，在函数中调用`reverse`反向解析函数，打印别名路径

```python
#都显示为/app01/index/
return HttpResponse(reverse('index'))
```

由于别名一样导致由于覆盖效果打印的同样的路径，都打印为`/app01/index/`，所以在项目的`urls.py中，为每一个路由分发配置命名空间namespace`

```python
urlpatterns = [
    #表示匹配app0x的路径，将其分发到app0x的urls.py文件下进行路由分发，并将其namespace设置为app0x
    re_path(r'app01/', include(('app01.urls','app01'))),
    re_path(r'app02/', include(('app02.urls','app02'))),
]
```

添加别名后，在视图函数中以namespace调用别名，打印路径就正确了

```python
#打印/app01/index/
def index(request):
    return HttpResponse(reverse('app01:index'))

#打印/app02/index/
def index(request):
    return HttpResponse(reverse('app02:index'))
```