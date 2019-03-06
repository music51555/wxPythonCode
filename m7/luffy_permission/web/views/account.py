from web.forms import MyForms
from django.shortcuts import render,redirect
from rbac.models import *
from django.contrib import auth

def login(request):

    if request.method == 'POST':
        form = MyForms.UserForms(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(len(username))
            print(len(password))

            user_obj = auth.authenticate(username=username, password=password)
            print(user_obj)

            if user_obj:
                auth.login(request, user_obj)
            else:
                wrong_err = '用户名或密码错误'
                return render(request, 'login.html', locals())

            url_queryset = UserInfo.objects.filter(
                username=username,roles__permissions__isnull=False).values('roles__permissions__url').distinct()

            url_list = [ item['roles__permissions__url'] for item in url_queryset ]

            request.session['user_permission_url'] = url_list

            return redirect('/customer/list/')

        else:
            if form.errors.get('__all__'):
                wrong_err = form.errors.get('__all__')[0]
            return render(request, 'login.html', locals())

    form = MyForms.UserForms()

    return render(request, 'login.html', locals())

def register(request):

    if request.method == 'POST':
        form = MyForms.UserForms(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            UserInfo.objects.create_user(username=username,password=password)

            return redirect('/login/')

    form = MyForms.UserForms()

    return render(request, 'register.html', locals())