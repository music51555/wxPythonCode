from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from setCookie.myforms import *
from django.contrib.auth.models import User

def login(request):

    if request.method=='POST':
        user=request.POST.get('username')
        pwd=request.POST.get('password')

        # 从auth_user表中验证用户名和密码，如果验证成功返回user对象，如果不成功返回None
        user_obj=auth.authenticate(username=user,password=pwd)

        # 如果验证成功，那么login接口最终源码实现逻辑是，得到了request.user=user，request.user这个对象将永远等于当前登录对象，如果没有调用login接口，如果没有登录成功，那么request.user默认是一个匿名对象AnonymousUser，也就是在auth_user中数据字段都为空的一条记录
        if user_obj:
            auth.login(request,user_obj)

        return redirect('/index/')

    form=UserForm()
    return render(request,'login.html',locals())

def index(request):

    # 输出用户对象的用户名和密码
    print(request.user.username)
    print(request.user.id)
    # 是否是匿名用户，执行了auth.login()后，就相当于执行request.user=user_obj，输出False，如果没有登录成功，则是匿名用户，输出True
    print(request.user.is_authenticated)

    print('User',User)

    # 如果执行了auth.login()函数了，那么request.user=user_obj，所以如果在直接访问index页面时，如果是非匿名函数则跳转index页，如果是匿名函数则跳转login页
    if request.user.is_authenticated:
        return render(request,'index.html',locals())
    else:
        return redirect('/login/')

def order(request):
    print(request.COOKIES)

    return HttpResponse('order')

def logout(request):
    # logout接口执行了注销功能，删除了session信息，底层执行request.session.flush()方法
    auth.logout(request)

    return redirect('/login/')

def register(request):

    if request.method=='POST':
        user=request.POST.get('username')
        pwd=request.POST.get('password')

        form=UserForm(request.POST)

        # 通过create_user()方法创建用户，插入数据后密码为加密状态，不是明文
        user_obj=User.objects.create_user(username=user,password=pwd)
        return redirect('/login/')

    form=UserForm()

    return render(request,'register.html',locals())

def forget_pwd(request):
    if request.method=='POST':
        username=request.POST.get('username')
        new_password=request.POST.get('new_username')

        user_obj=User.objects.get(username=username)
        print('user_obj',user_obj)
        user_obj.set_password(password=new_password)
        user_obj.save()

        return redirect('/login/')

    return render(request,'forget_pwd.html')