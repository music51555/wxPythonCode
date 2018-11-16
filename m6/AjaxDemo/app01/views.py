from django.shortcuts import render,HttpResponse
from django.db.models import Q
from app01.models import *
import json

def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
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

def upload(request):
    if request.method == 'POST':
        # 输出<MultiValueDict: {'upload': [<InMemoryUploadedFile: 拆分文件.png (image/png)>]}>
        print(request.FILES)
        # 通过HTML上传文件input标签的name属性，得到文件对象，打印文件对象输出文件名
        file_obj=request.FILES.get('upload')

        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)

    return render(request,'upload.html')