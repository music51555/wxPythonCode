Django之类视图函数



创建自定义类视图，其中的函数方法，必须为http请求的方法名

```python
from django.views import View
from django.shortcuts import HttpResponse

class my_views(View):

    def get(self,request):

        return HttpResponse('Hello world')
```



在路由分发中配置

```python
urlpatterns = [
	path('my_views',my_views.as_view()),
]
```
