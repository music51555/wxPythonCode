from django.shortcuts import render
import datetime

def timer(request):
    ctime = datetime.datetime.now().strftime('%Y-%m-%d %X')
    return render(request,'timer.html',{"ctime":ctime})

def login(request):
    return render(request,'login.html')