from django.shortcuts import render,HttpResponse
import datetime

def timer(request):
    ctime = datetime.datetime.now().strftime('%Y-%m-%d %X')
    return render(request,'timer.html',{"ctime":ctime})

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        print(request.POST)
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'wangxin' and password == '123456':
            return HttpResponse('登录成功')
        else:
            return HttpResponse('用户名或密码错误')

def special_case_2003(request):
    return HttpResponse('<h1>hello</h1>')

def year_archive(request,year):
    return HttpResponse(year)

def year_month_archive(request,year,month):
    return HttpResponse(year+'-'+month)