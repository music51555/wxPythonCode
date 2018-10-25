from django.urls import path,re_path,include
from app01 import views

urlpatterns = [
    path('timer/', views.timer),
    path('login/', views.login),

    # 通过正则表达式匹配URL路径，调用视图函数
    # ^articles/2003/$表示匹配以articles开头，以2003/结尾的路径，并调用special_case_2003(request)函数
    re_path(r'^articles/2003/$', views.special_case_2003,name='s_c_2003'),
    re_path(r'^articles/([0-9]{4})/$', views.year_archive,name='y_a'),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.year_month_archive),
    re_path('index/',views.index,name='index')
]