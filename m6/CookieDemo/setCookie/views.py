from django.shortcuts import render,redirect,HttpResponse
from setCookie.myforms import *

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

    login_status=request.COOKIES.get('login')
    username=request.COOKIES.get('username')
    if login_status:
        return render(request,'index.html',locals())
    else:
        return redirect('/login/')

def order(request):
    print(request.COOKIES)

    return HttpResponse('order')