from django.shortcuts import render,HttpResponse,redirect
from app01.myforms import *

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
    # {'is_login': 'True'}
    print(request.COOKIES)

    is_login=request.COOKIES.get('is_login')

    if is_login:
        username = request.COOKIES.get('username')
        return render(request,'index.html',locals())
    else:
        return redirect('/login/')