设置cookie参数

**1、max_age=15**，15秒后cookie失效

**2、expires=data**，到达指定日期后cookie失效

```python
def login(request):
    if request.method=='POST':
        form=UserForm(request.POST)

        username=request.POST.get('username')
        password=request.POST.get('password')

        if form.is_valid():
            user_obj = User.objects.filter(username=username, password=password).first()

            response=redirect('/index/')

            # 1、30秒后login的cookie失效,max_age=15秒后失效
            response.set_cookie('login',True,max_age=30)

            import datetime
            data=datetime.datetime(year=2018,month=11,day=23,hour=6,minute=37)
            # 2018年11月23日，当前hour-8表示当前时间，37分cookie失效
            # 2、expires  /ek- ɪk'spaɪɚz/ 有效期，到达指定有效期后cookie失效
            response.set_cookie('login',True,expires=data)

            response.set_cookie('username',user_obj.username,)
            return response
        else:
            error=form.errors.get('__all__')
            response=render(request,'login.html',locals())
            response.set_cookie('login',False)
            return response
```



**3、path**

设置cookie的有效路径

```python
def login(request):
    if request.method=='POST':
        form=UserForm(request.POST)

        username=request.POST.get('username')
        password=request.POST.get('password')

        if form.is_valid():
            user_obj = User.objects.filter(username=username, password=password).first()

            response=redirect('/index/')
            # path='/'表示对网站下任何路径cookie都起作用
            # response.set_cookie('login',True,path='/')
            # path='/index'表示cookie只在/index路径下才生效
            response.set_cookie('login',True,path='/index')
            response.set_cookie('username',user_obj.username,)
            return response
        else:
            error=form.errors.get('__all__')
            response=render(request,'login.html',locals())
            response.set_cookie('login',False)
            return response

    form=UserForm()
    return render(request,'login.html',locals())
```



登录成功后跳转至index页面，在请求cookie中包含了login的cookie

![1542964156000](.\images\1542964156000.png)

再次访问order页面，在请求参数中，没有显示已存在的login的cookie，因为它的有效路径是index页

![1542964227487](.\images\1542964227487.png)