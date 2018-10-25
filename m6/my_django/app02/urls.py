from django.urls import re_path
from app02 import views

urlpatterns = [
    re_path('index/',views.index,name='index')
]