在登录页如果校验用户名和密码成功，则创建响应体对象`response`，并为响应体`set_cookie`设置cookie

```python
def login(request):

    if request.method=='POST':
        form=UserForm(request.POST)

        username=request.POST.get('username')
        password=request.POST.get('password')

        user_obj=User.objects.filter(username=username,password=password)
        # 通过查询出的user对象，设置列名username的值
        username=response.set_cookie('username',user_obj.username)

        if user_obj:
            response=HttpResponse('登录成功')
            response.set_cookie('is_login',True)
            return response

        return render(request,'login.html',locals())
```



登录成功后，服务器返回响应数据“登录成功”，并在`Response Cookies`中设置了cookie信息`is_login=True`

![cookie1](./images/cookie1.png)

此时发送请求访问其他页面index，浏览器响应头中仍保存着cookie信息，但这是在`Request Cookies`中，因为index视图函数中，并没有操作cookie信息，所以响应体中不包含cookie信息

![image-20181122215651311](./images/cookie2.png)

访问其他页面时，检查cookie信息，如果有is_login的cookie，那么就允许用户访问index页面，否则将跳转回login页面，使用其他浏览器访问时，由于没有cookie信息，会直接重定向到login页面

```python
def index(request):
    # {'is_login': 'True'}
    print(request.COOKIES)
	
    # 读取cookie信息
    is_login=request.COOKIES.get('is_login')
    # 发送到HTML网页后可以通过HI，{{ username }}实现打印HI，alex
	username=request.COOKIES.get('username')

    if is_login:
        return render(request,'index.html')
    else:
        return redirect('/login/')
```

