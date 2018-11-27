**session：**服务器将key-value存储到服务端



**设置session**：`request.session['is_login']=True`

**读取session**：`is_login=request.session['is_login']`



**创建过程：**

1、客户端第一次请求，依然是携带`cookie,{ }`

2、服务器设置执行`request.session['username']='alex'`，并为当前`session`生成随机字符串的`sessionid`

3、在底层代码逻辑中，响应体中设置`set_cookie（'sessionid'，随机字符串）`

4、在`django_session`表中添加内容：随机字符串的`sessionid：{'is_login':True,'username':'alex'}`

**代码逻辑：**

```python
def login_session(request):

    username=request.POST.get('username')
    password=request.POST.get('password')

    form = UserForm()
    user_obj=User.objects.filter(username=username).first()

    if user_obj:
        # session_key:cwii0iigbkihz83yw7yvf2wrlfgw5p5x
        # session_data:ODc2MWY1NzZiZWIyN...(被加密)，是一个字典形式
        
        # 服务器执行该句时，生成了随机的sessionid，如cwii0iigbkihz83yw7yvf2wrlfgw5p5x，并执行response.set_cookie('sessionid',随机字符串)
        request.session['is_login']=True
        request.session['username']=user_obj.username
        
	   # 返回响应体时，服务器设置了set_cookie(sessionid,)		
        return HttpResponse('登录成功')

    return render(request,'login.html',locals())
```



服务器在响应体中设置了key为sessionid的cookie，值为随机生成的sessionid字符串：

![1543204627924](.\images\1543204627924.png)



在`django_session`表中添加了数据

![1543204705477](.\images\1543204705477.png)



**使用过程：**

1、`request.session.get('is_login')`的过程是，先通过`request.COOKIES.get('sessionid')`，得到`session_key`

2、`django_session`表中按照`session_key`的值`cwii0iigbkihz83yw7yvf2wrlfgw5p5x`过滤`session_data`

3、通过`session_data.get（'is_login'）`取出`session`数据

**代码逻辑：**

```python
def index(request):

    # 底层通过request.COOKIES.get('sessionid')读取session_key
    # 在django_session表中过滤数据，取出session_data字典
    # 在字典中取出数据
    login_status=request.session.get('is_login')
    username=request.session.get('username')

    if login_status:
        return render(request,'index.html',locals())
```

