"""my_django URL Configuration

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
from django.urls import path,re_path,include,register_converter
from app01 import views
from app01.Rex_Mons import Mons

register_converter(Mons,'rm')

urlpatterns = [
    path('Log/',views.login,name = 'Log'),
    path('timer/',views.timer),

    # 表示当在URL路径下遇到app01路径时，被分发到哪个应用下去查找视图函数
    re_path(r'app01/', include(('app01.urls','app01'))),
    re_path(r'app02/', include(('app02.urls','app02'))),
    # 表示在路径下遇到任何开头时，后面路径被分发到aoo01.urls下去查找视图函数
    # re_path(r'^', include('app01.urls')),
    #path('articles/<path:year>/',views.index),
    path('index/',views.index),
    path('articles/<rm:month>/',views.index),
]
