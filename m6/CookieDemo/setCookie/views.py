from django.shortcuts import render
from setCookie.myforms import *

def login(request):

    if request.method=='POST':
        form=UserForm(request.POST)

        # 只有调用了is_valid方法，才会执行UserForm自定义类中的clean全局钩子函数。
        if form.is_valid():
            response = render(request, 'index.html', locals())
            response.set_cookie('login',True)

            return response
        else:
            error=form.errors.get('__all__')
        return render(request, 'login.html', locals())

    form=UserForm()
    return render(request,'login.html',locals())