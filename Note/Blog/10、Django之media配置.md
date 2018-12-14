`Django`之`media`配置

**静态文件分为两种：**

**1、`static`**：服务器使用的静态文件，如`js、css、img`等

**2、`media`**：用户上传的文件



**知识点1：**`MEDIA_ROOT`表示用户通过表中`FileField`、`ImageField`上传文件保存的路径，一般叫做`media`文件夹

**知识点2：**发现不填写`MEDIA_URL`就可以访问通过路由配置的`media`下的图片，且网上说设置了`MEDIA_URL`后可以在HTML网页中通过`{{ MEDIA_URL }}`访问该路径



一、在`settings.py`中配置`Media`路径

```python
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
```



二、创建表时使用`FileField、ImageField`等类型字段

```python
class UserInfo(AbstractUser):
    avatar=models.FileField(upload_to='avatars/',default='/avatars/default.png')
```



三、**一旦定义`upload_to`上传字段，那么在创建用户时，`Django`会将文件保存至`MEIDA_ROOT`所配置的文件夹中**

按照`upload_to='avatars/'`定义的路径，在`media`文件夹下**先**创建文件夹，**再**保存图片

![1544500999181](.\image\1544500999181.png)



但是需要判断用户是否上传了头像，如果没有上传，那么通过`request.FILES.get('avatar')`得到的是`None`，新建用户后头像字段为空

```python
def register(request):
    response = {'user': None, 'msg': None}

    if request.is_ajax():
        form = myForms.UserForm(request.POST)

        if form.is_valid():
            response['user'] = form.cleaned_data.get('username')

            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            avatar_obj=request.FILES.get('avatar')
            
            # 增加用户是否上传了图片的判断
            if avatar_obj:
                UserInfo.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    avatar=avatar_obj
                )
            else:
                UserInfo.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                )
        else:
            response['msg'] = form.errors

        return JsonResponse(response)

    form = myForms.UserForm()
    return render(request, 'register.html', locals())
```



访问`http://127.0.0.1:8001/static/img/default.jpg`**可以**浏览到图片，是因为开放了`static`路径的访问权限

访问`http://127.0.0.1:8001/media/avatars/大象家园.jpg`**无法**浏览到图片

访问`http://127.0.0.1:8001/media/blog/views.py`**无法**访问到代码文件，否则会轻而易举的访问到代码文件

`Django`在`settings.py`中通过配置`STATIC_URL='/static/'`，让用户可以访问到静态文件

默认访问路径都是通过`url.py`文件路由分发的



**开放`media`访问路径访问权限：**

一、`settings.py`添加配置

```python
MEDIA_URL = '/media/'
```



二、`url.py`路由分发配置

```python
from django.views.static import serve
from MyBlog import settings

# (?P<path>.*)分组后起别名path+固定格式，^表示匹配开头，之所以给分组设置path变量，是因为serve方法需要一个path变量，不设置会报serve() missing 1 required positional argument: 'path'
re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})
```



但是发现没有在`settings.py`中设置`MEDIA_URL`也可以访问到

最后浏览到`media`下的文件

![1544510469881](.\image\1544510469881.png)