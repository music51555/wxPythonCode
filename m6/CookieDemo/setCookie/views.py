from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from setCookie.myforms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method=='POST':
        user=request.POST.get('username')
        pwd=request.POST.get('password')

        user_obj=auth.authenticate(username=user,password=pwd)


        if user_obj:
            auth.login(request,user_obj)

        # 捕获装饰器跳转路径中的get请求参数next
        next_url = request.GET.get('next')

        # 如果通过装饰器捕获到next参数，则跳转到next地址，如果直接通过login地址登录，则跳转至index页面
        if next_url:
            return redirect(next_url)
        else:
            return redirect('/index/')

    print('login')
    form=UserForm()
    return render(request,'login.html',locals())

@login_required
def index(request):

    # 输出用户对象的用户名和密码
    print(request.user.username)
    print(request.user.id)
    # 是否是匿名用户，执行了auth.login()后，就相当于执行request.user=user_obj，输出False，如果没有登录成功，则是匿名用户，输出True
    print(request.user.is_authenticated)

    print('User',User)

    return render(request,'index.html')

@login_required
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
        old_password=request.POST.get('password')
        new_password=request.POST.get('new_password')

        form=UserForm(request.POST)
        print('post')
        if form.is_valid():
            user_obj=User.objects.get(username=username)

            # check_password方法在用户修改密码时，传入旧密码参数，来校验是否与旧密码相匹配，如果相匹配再允许用户去修改密码，否则不允许修改密码
            if user_obj.check_password(old_password):
                print('旧密码验证正确')

                print('user_obj', user_obj)
                user_obj.set_password(new_password)
                user_obj.save()

                return redirect('/login/')
            else:
                print('旧密码验证失败')
        else:
            print('error',form.errors)
            return render(request,'forget_pwd.html',locals())

    form=UserForm()
    return render(request,'forget_pwd.html',locals())