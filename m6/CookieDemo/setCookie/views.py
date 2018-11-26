from django.shortcuts import render,redirect,HttpResponse
from setCookie.myforms import *
import datetime

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
            response.set_cookie('login',True,path='/index/')
            response.set_cookie('username',user_obj.username,)
            return response
        else:
            error=form.errors.get('__all__')
            response=render(request,'login.html',locals())
            response.set_cookie('login',False)
            return response

    form=UserForm()
    return render(request,'login.html',locals())

def index(request):

    # 底层通过request.COOKIES.get('sessionid')读取session_key
    # 在django_session表中过滤数据，取出session_data字典
    # 在字典中取出数据
    login_status=request.session.get('is_login')
    username=request.session.get('username')
    last_time=request.session.get('last_time')
    if last_time:
        last_login=last_time
    else:
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        request.session['last_time']=now

    if login_status:
        return render(request,'index.html',locals())
    else:
        return redirect('/login/')

def order(request):
    print(request.COOKIES)

    return HttpResponse('order')

def login_session(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        form=UserForm(request.POST)

        user_obj=User.objects.filter(username=username,password=password).first()

        if user_obj:
            request.session['is_login']=True
            request.session['username']=user_obj.username

            return redirect('/index/')

    form = UserForm()
    return render(request,'login.html',locals())

def logout(request):
    # 删除session_data字典中的某个键值
    # del request.session['last_time']

    request.session.flush()

    return redirect('/login/')