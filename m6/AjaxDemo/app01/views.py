from django.shortcuts import render,HttpResponse
from app01.models import *
from django.core.paginator import Paginator
from django import forms

def upload(request):

    if request.method == 'POST':
        print(request.POST)
        file_obj=request.FILES.get('upload')
        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

    return render(request,'upload.html')

def index(request):

    book_list=Book.objects.all()

    paginator=Paginator(book_list,8)
    current_page_num=int(request.GET.get('page'))
    current_page=paginator.page(current_page_num)
    page_range=paginator.page_range

    if paginator.num_pages<11:
        page_range=paginator.page_range
    elif current_page_num-5<=0:
        page_range=range(1,12)
    elif current_page_num+5>paginator.num_pages:
        page_range=range(paginator.num_pages-10,paginator.num_pages+1)
    else:
        page_range=range(current_page_num-5,current_page_num+6)

    return render(request,'book_list.html',locals())

class UserForm(forms.Form):
    username=forms.CharField(min_length=4,label='用户名')
    password=forms.CharField(min_length=4,label='密码')
    email=forms.EmailField(label='邮箱')

def register(request):
    form=UserForm(request.POST)

    if form.is_valid():
        print(form.cleaned_data)
    else:
        print(form.cleaned_data)
        print(form.errors)
        print(form.errors.get('password')[0])
        print(form.errors.get('email')[0])

    return render(request,'register.html',locals())