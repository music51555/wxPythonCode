from web.forms import MyForms
from django.shortcuts import render,redirect
from django.contrib import auth

def login(request):

    if request.method == 'POST':
        form = MyForms.UserForms(request.POST)

        if form.is_valid():
            user_obj = auth.authenticate(
                username = request.POST.get('username'),
                password = request.POST.get('password')
            )

            if user_obj:
                auth.login(request.user)
                return redirect('/customer/list/')
            else:
                return render(request, 'login.html', locals())

        else:
            return render(request, 'login.html', locals())

    form = MyForms.UserForms()

    return render(request, 'login.html', locals())