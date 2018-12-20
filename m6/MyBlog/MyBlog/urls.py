"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog import views
from MyBlog import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('comment/', views.comment),
    path('get_comment_tree/', views.get_comment_tree),
    path('backend/', views.backend),
    path('add_article/', views.add_article),
    # 以^开头，就表示以根路径开头，分组后，就会得到用户输入的内容，存储到别名username上
    re_path('^(?P<username>\w+)/$', views.home_site),
    re_path('^$', views.index),
    path('register/', views.register),
    path('get_validCode_img/', views.get_valid_code_img),
    re_path('^(?P<username>\w+)/article/(?P<article_id>\d+)/$',views.article_detail),

    # (?P<path>.*)分组后起别名path+固定格式
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)$', views.home_site)
]