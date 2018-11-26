- 如何设置时区：在setting.py中`TIME_ZONE = Asia/Shanghai`

- 如果可以取到cookie值，使用该值，如果取不到，则默认为空

```python
request.COOKIES.get('last_time'，'')
```



访问成功跳转index页后，设置当前登录时间，下次再次登录成功，跳转index页面后，就可以获取上次设置的登录时间，进行显示

```python
def index(request):

    is_login=request.COOKIES.get('is_login')

    if is_login:
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 获取上一次的访问时间，如果可以获取到key值，就以key值为准，如果获取不到key值，默认为空
        last_time=request.COOKIES.get('last_time','')

        # 设置当前时间为最后登录时间，设置cookie值last_time，下次登录时取该值，作为上次登录时间显示
        response=render(request,'index.html',locals())
        response.set_cookie('last_time',now)
        
        username = request.COOKIES.get('username')
        return response
    else:
        return redirect('/login/')
```



在HTML中获取

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>HI,{{ username }}</h3>
<p>上次登录时间:{{ last_time }}</p>
</body>
</html>
```

