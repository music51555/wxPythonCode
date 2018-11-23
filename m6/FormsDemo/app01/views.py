from django.shortcuts import render
from app01.myforms import *

def register(request):
    if request.method=='POST':

        form=RegisterForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
            error=form.errors.get('__all__')

        return render(request,'register.html',locals())

    form=RegisterForm()
    return render(request,'register.html',locals())