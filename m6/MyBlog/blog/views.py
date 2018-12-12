from django.shortcuts import render, HttpResponse, redirect
import os
from django.http import JsonResponse
from django.contrib import auth
from blog import myForms
from blog.models import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
valid_img_bgc = os.path.join(BASE_DIR, 'static', 'valid_img_bgc', 'valid_bgc.png')


def login(request):
    response = {'user': None, 'msg': None}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_code = request.POST.get('valid_code')

        if valid_code.lower() == request.session['valid_code'].lower():
            # 通过auth.authenticate来验证用户名和密码是否正确，如果校验正确则返回的对象为当前用户的用户名alex，如果错误则为None
            user = auth.authenticate(username=username, password=password)
            if user:
                # ajax提交的请求如果校验正确，不要想着return一个跳转页面，因为在ajax的success函数中接收的是一个data字段，如果校验正确，在ajax中通过location.href='/index'来跳转
                auth.login(request, user)
                response['user'] = username
            else:
                response['msg'] = '用户名或密码错误'

            return JsonResponse(response)
        else:
            response['msg'] = '验证码错误'

            return JsonResponse(response)

    return render(request, 'login.html')


def index(request):

    article_list = Article.objects.all()

    return render(request, 'index.html', locals())

def home_site(request, username):

    user=UserInfo.objects.filter(username=username).first()

    if not user:
        return render(request, 'not_found.html')
    else:
        # 正向查询按字段，是因为在定义表结构时，该表中就有与另一个表相关的外键列，所以通过有另一个表中字段的表去查询另一个表，就是正向查询，正向查询按字段。反之就是反向查询，以对象的形式查询时，反向查询按表名_set，如user_obj.article_set.all()
        # 输出<QuerySet [<Article: selenium之表格的定位>, <Article: 异步编程之使用yield from>]>
        article_list = user.article_set.all()

        # 基于双下划线的跨表查询
        # 输出<QuerySet [<Article: selenium之表格的定位>, <Article: 异步编程之使用yield from>]>
        article_list = Article.objects.filter(user=user)

        return HttpResponse('OK')


def logout(request):
    auth.logout(request)

    return redirect('/login/')


def get_valid_code_img(request):
    from blog.utils import get_valid_code

    data = get_valid_code.get_valid_code_img(request)

    return HttpResponse(data)


def register(request):
    response = {'user': None, 'msg': None}

    if request.is_ajax():
        form = myForms.UserForm(request.POST)

        if form.is_valid():
            response['user'] = form.cleaned_data.get('username')

            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            avatar_obj = request.FILES.get('avatar')

            extra_fields = {}
            if avatar_obj:
                extra_fields = {'avatar': avatar_obj}

            # 优化冗余的代码结构，传递附加的额外字段
            UserInfo.objects.create_user(username=username, password=password, email=email, **extra_fields)

        else:
            response['msg'] = form.errors

        return JsonResponse(response)

    form = myForms.UserForm()
    return render(request, 'register.html', locals())
