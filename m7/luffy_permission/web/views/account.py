from web.forms import MyForms
from django.shortcuts import render,redirect
from rbac.models import *
from django.contrib import auth

def login(request):

    if request.method == 'POST':
        form = MyForms.UserForms(request.POST)

        if form.is_valid():

            username = request.POST.get('name')
            password = request.POST.get('password')

            user_obj = auth.authenticate(username=username, password=password)

            auth.login(request, user_obj)

            url_queryset = UserInfo.objects.filter(
                name=request.POST.get('name'),roles__permissions__isnull=False).values('roles__permissions__url').distinct()

            url_list = [ item['roles__permissions__url'] for item in url_queryset ]

            request.session['user_permission_url'] = url_list

            return redirect('/customer/list/')

        else:
            if form.errors.get('__all__'):
                wrong_err = form.errors.get('__all__')[0]
            return render(request, 'login.html', locals())

    form = MyForms.UserForms()

    return render(request, 'login.html', locals())