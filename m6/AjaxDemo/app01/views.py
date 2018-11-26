from django.shortcuts import render,HttpResponse,redirect
from app01.myforms import *
import datetime

def login(request):

    if request.method=='POST':
        form=UserForm(request.POST)

        username=request.POST.get('username')
        password=request.POST.get('password')

        user_obj=User.objects.filter(username=username,password=password).first()

        if user_obj:
            response=HttpResponse('登录成功')
            response.set_cookie('is_login',True)
            response.set_cookie('username',user_obj.username)
            return response

        return render(request,'login.html',locals())

    form=UserForm()

    return render(request,'login.html',locals())

def index(request):

    if request.method=='POST':
        fruit=request.POST.getlist('fruit')

        response = HttpResponse('ok')
        response.set_cookie('fruit',fruit)

        return response

    is_login=request.COOKIES.get('is_login')

    if is_login:
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 获取上一次的访问时间，如果可以获取到key值，就以key值为准，如果获取不到key值，默认为空
        last_time=request.COOKIES.get('last_time','')

        fruit=request.COOKIES.get('history','')
        print('fruit',fruit)

        # 设置当前时间为最后登录时间，设置cookie值last_time，下次登录时取该值，作为上次登录时间显示
        response=render(request,'index.html',locals())
        response.set_cookie('last_time',now)
        username = request.COOKIES.get('username')
        fruit = request.COOKIES.get('fruit')
        print('username',username)
        print('fruit',fruit)
        return response
    else:
        return redirect('/login/')