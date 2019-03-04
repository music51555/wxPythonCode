from django.shortcuts import render, HttpResponse, redirect
import os
from django.http import JsonResponse
from django.contrib import auth
from blog import myForms
from blog.models import *
from django.db.models import F
from django.db import transaction
from django.contrib.auth.decorators import login_required
from MyBlog import settings
from bs4 import BeautifulSoup
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import *
from django.db.models import Count
from blog.My_field import *

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

            print(JsonResponse(response).getvalue())

            return JsonResponse(response)

    return render(request, 'login.html')


def index(request):
    article_list = Article.objects.all()

    obj=Article.objects.annotate(month=TruncMonth('create_time')).values('month').annotate(count=Count('nid')).values_list('month','count')
    print(obj)

    return render(request, 'index.html', locals())


def home_site(request, username, **kwargs):

    # 首先判断是否有当前在URL中访问的用户
    user = UserInfo.objects.filter(username=username).first()
    user = UserInfo.objects.get(username = username)
    blog = user.blog

    if not user:
        # 如果用户不存在，那么返回not_found.html页面
        return render(request, 'not_found.html')
    else:

        if kwargs:
            condition = kwargs.get('condition')
            param = kwargs.get('param')

            if condition == 'tag':
                article_list = Article.objects.filter(tags__title=param, user=user)
            elif condition == 'category':
                article_list = Article.objects.filter(category__title=param, user=user)
            else:
                year = param.split('/')[0]
                month = param.split('/')[1]
                article_list = Article.objects.filter(create_time__year=year, create_time__month=month, user=user)
        else:
            article_list = Article.objects.filter(user=user)

        return render(request, 'home_site.html', locals())


@login_required
def backend(request):

    article_list = Article.objects.filter(user=request.user)

    return render(request, 'backend_manage.html', locals())


def add_article(request):
    user=UserInfo.objects.filter(username=request.user.username).first()

    if request.method == 'POST':
        article_title=request.POST.get('article-title')
        article_content=request.POST.get('article-content')
        category=request.POST.get('category')
        tag=request.POST.getlist('tag')

        # 通过html.parser解析器得到文章内容+标签对象soup
        soup = BeautifulSoup(article_content, 'html.parser')

        # find_all结果是一个列表，存储每一对标签和标签值[<p>hello</p>, <p>world</p>, <p><br/></p>, <br/>, <script>alert(123)</script>]
        # 每一个标签对象都有name属性，判断其值是否等于非法标签内容，调用标签对象的decompose方法将其删除，删除后soup对象中就不包含非法内容了
        for tag in soup.find_all():
            if tag.name == 'script':
                tag.decompose()

        desc = soup.text[:150].strip()

        # 存储文章内容时，直接使用去除非法标签后的str(soup)对象内容
        article_obj=Article.objects.create(
            title=article_title, desc=desc, content=str(soup), user_id=request.user.pk,category_id=category)
        for i in tag:
            Article2Tag.objects.create(article_id=article_obj.pk,tag_id=i)

    cate_list = Category.objects.filter(blog=user.blog)
    tag_list = Tag.objects.filter(blog=user.blog)

    return render(request, 'add_article.html', locals())


def logout(request):
    auth.logout(request)

    return redirect('/login/')


def get_valid_code_img(request):
    from blog.utils import get_valid_code

    data = get_valid_code.get_valid_code_img(request)

    return HttpResponse(data)


def article_detail(request, username, article_id):
    user = UserInfo.objects.filter(username=username).first()
    article_obj = Article.objects.filter(nid=article_id, user_id=user.nid).first()

    blog = user.blog

    # 视频中使用state判断
    ret = {'msg': None, 'tag': None}

    if request.is_ajax():
        article_title = request.POST.get('article_title')
        tag = request.POST.get('tag')

        article_obj = Article.objects.filter(title=article_title,user_id=user.nid).first()
        # 先在点赞和踩灭表中判断用户是否针对当前文章做过点赞或踩灭操作，用于在后面判断是否允许用户再对该篇文章再进行点赞或踩灭操作
        digg_bury_record = ArticleUpDown.objects.filter(
            article_id=article_obj.nid, user_id=request.user.nid).exists()

        ret['tag'] = tag

        # 重复在文章表中按用户和文章标题过滤出文章，更新up_count和down_count的值时，可以提取出queryset，在后面调用
        query_article = Article.objects.filter(user=user, title=article_title)

        if not digg_bury_record:
            if tag == 'diggit':
                    ArticleUpDown.objects.create(
                        article_id=article_obj.nid, user_id=request.user.nid, is_up=True)
                    query_article.update(up_count=F('up_count')+1)
                    ret['msg'] = '推荐成功'
            else:
                if not digg_bury_record:
                    ArticleUpDown.objects.create(
                        article_id=article_obj.nid, user_id=request.user.nid, is_up=False)
                    # 在update中如果要对列值做加减运算，可以使用F函数，取得当前列值后，做+1操作
                    query_article.update(down_count=F('down_count')+1)
                    ret['msg'] = '反对成功'
        else:
            is_up = ArticleUpDown.objects.filter(
                article_id=article_obj.nid, user_id=request.user.nid).values_list('is_up').first()

            if is_up[0] == True:
                ret['msg'] = '您已经推荐过了'
            else:
                ret['msg'] = '您已经反对过了'

        return JsonResponse(ret)
    else:
        print(article_obj.pk, user.pk)
        comment_obj=Comment.objects.filter(article_id=article_obj.pk)

    print(comment_obj)

    return render(request, 'article_detail.html', locals())


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


def comment(request):
    ret = {'comment_content': None}
    if request.method == 'POST':

        article_id = request.POST.get('article_id')
        comment_content = request.POST.get('comment_content')
        parent_pid = request.POST.get('parent_pid')

        article_obj = Article.objects.filter(pk=article_id).first()

        # 如果评论有父评论，那么久判断parent_pid是否是数字，进行转换
        if parent_pid.isdigit():
            parent_pid = int(parent_pid)
        else:
            print(parent_pid)

        with transaction.atomic():
            comment_obj = Comment.objects.create(
                article_id=article_id, content=comment_content, user_id=request.user.pk, parent_comment_id=parent_pid)
            Article.objects.filter(pk=article_id).update(comment_count=F('comment_count')+1)

        ret['comment_content'] = comment_content
        ret['create_time'] = comment_obj.create_time.strftime('%Y-%m-%d %X')

        import threading
        from django.core.mail import send_mail
        from MyBlog.settings import EMAIL_HOST_USER
        t = threading.Thread(target=send_mail, args=('您的%s文章收到一条新评论'%article_obj.title,
                                                  comment_content,
                                                  EMAIL_HOST_USER,
                                                  ['452427904@qq.com', ]
                                                  ))
        t.start()

        return JsonResponse(ret)


def get_comment_tree(request):
    article_id = request.GET.get('article_id')
    comment_list = list(Comment.objects.filter(article_id=article_id).values('pk', 'content', 'parent_comment'))

    return JsonResponse(comment_list, safe=False)


def upload(request):

    file_obj=request.FILES.get('upload_img')

    path=os.path.join(settings.MEDIA_ROOT, 'upload', file_obj.name)

    with open(path, 'wb') as f:
        for line in file_obj:
            f.write(line)

    # 给编辑器返回一个字典，key-value不能变，可变的是文件名称
    response = {
        'error': 0,
        'url': 'media/upload/'+file_obj.name
    }

    return JsonResponse(response)
