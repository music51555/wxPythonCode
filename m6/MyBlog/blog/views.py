from django.shortcuts import render, HttpResponse
import os
from django.http import JsonResponse
from django.contrib import auth
from blog import myForms

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
    return render(request, 'index.html', locals())


def get_validCode_img(request):
    from blog.utils import get_valid_code

    data = get_valid_code.get_valid_code_img(request)

    return HttpResponse(data)


def register(request):
    response = {'user': None, 'msg': None}

    if request.is_ajax():
        form = myForms.UserForm(request.POST)

        if form.is_valid():
            response['user'] = form.cleaned_data.get('username')

            return JsonResponse(response)
        else:
            response['msg'] = form.errors

            return JsonResponse(response)

    form = myForms.UserForm()
    return render(request, 'register.html', locals())
