from django.shortcuts import render, HttpResponse, redirect
import os
from django.http import JsonResponse
from django.contrib import auth
from blog import myForms
from blog.models import *
from django.db.models import Count

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

    # 首先判断是否有当前在URL中访问的用户
    user = UserInfo.objects.filter(username=username).first()

    if not user:
        # 如果用户不存在，那么返回not_found.html页面
        return render(request, 'not_found.html')
    else:
        article_list = user.article_set.all()

        article_list = Article.objects.filter(user=user)

        # 查询当前站点每一个分类下的文章数，Category分类表中有blog字段，是外键列一对多关系，利用当前user按对象跨表查询出站点对象，并给予主键分组，通过聚合函数跨表统计查询文章总数，展示出分类名和对应的文章总数
        cate_arti_coutn=Category.objects.filter(blog=user.blog).values('pk').annotate(article_count=Count('article__nid')).values('title','article_count')
        print(cate_arti_coutn)

        # 查询当前站点每一个标签下的文章数，Article文章表中有tags字段，是多对多关系，反向查询按表名，写为article__nid
        tag_arti_count=Tag.objects.filter(blog=user.blog).values('nid').annotate(c=Count('article__nid')).values('title', 'c')
        print(tag_arti_count)

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
