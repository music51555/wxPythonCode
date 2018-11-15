from django.shortcuts import render,HttpResponse
from django.db.models import Q
from app01.models import *

def index(request):

    return render(request,'index.html')

def login(request):

    username=request.POST.get('username')
    password=request.POST.get('password')

    ret={"username":None,"message":None}
    user_obj=User.objects.filter(Q(username=username)&Q(password=password))
    if user_obj:
        ret['username']=username
    else:
        ret['message']='username or password wrong!'

    import json
    jsonret=json.dumps(ret)

    return HttpResponse(jsonret)