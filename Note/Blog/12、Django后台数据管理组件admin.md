`Django`后台数据管理组件`admin`

`Django`提供了一个后台管理页面，使用超级用户访问`http://127.0.0.1:8001/admin`页面，用于管理所有已创建的表，可以对表数据进行管理，前期是必须要先注册各个表

![1544581812525](C:\Users\ADMINI~1\AppData\Local\Temp\1544581812525.png)



**创建超级用户的命令：**

`python3 manage.py createsuperuser`创建超级用户后，会在`auth`对应的用户表中创建超级用户



**注册管理表**

在`app/admin.py`下注册创建的表

```python
from django.contrib import admin
from blog import models

# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Article)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article2Tag)
admin.site.register(models.Comment)
```



再次查看`admin`页面

![1544582264476](.\image\1544582264476.png)



可以在此新增文章：

![1544582448018](.\image\1544582448018.png)