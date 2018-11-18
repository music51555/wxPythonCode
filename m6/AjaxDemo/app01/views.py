from django.shortcuts import render,HttpResponse
from django.db.models import Q
from app01.models import *
from django.core.paginator import Paginator,EmptyPage
from django import forms

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

def page(request):
    book_list=Book.objects.all()
    # 控制每页显示几条数据
    paginator=Paginator(book_list,5)

    try:
        current_page_num=int(request.GET.get('page'))
        current_page=paginator.page(current_page_num)

        if paginator.num_pages > 11:
            # 在只显示11个页码时，如果点击的页数<=0了，就不应该去显示0页、-1页...了，直接定义为显示1--11页
            if current_page_num-5<=0:
                page_range=range(1,12)
            # 如果点击的页数+5，如16页，超出了20页的范围，就不应该显示21页、22页...了，直接使用range(最大页数-10，最大页数+1)，显示最后11页的页码
            elif current_page_num+5>paginator.num_pages:
                page_range=range(paginator.num_pages-10,paginator.num_pages+1)
            # 最后是正常显示左5，右5的页码，直接定义为range(当前页-5，当前页+6)
            else:
                page_range=range(current_page_num - 5, current_page_num + 6)
        else:
            # 如果没有超出11页，那么就默认使用page_range的页码列表就可以了
            page_range=paginator.page_range

    except EmptyPage as e:
        current_page=paginator.page(1)

    return render(request,'page.html',locals())

class UserForm(forms.Form):
    # 定义的所有变量必须和HTML的form表单中的name匹配，才会去进行验证
    username=forms.CharField(min_length=4)
    password=forms.CharField(min_length=4)
    email=forms.EmailField()

def register(request):

    if request.method=='POST':
        print(request.POST)

        # 可以自己手动传入参数进行测试，参数是字典形式
        # form=UserForm({"username":"wang","email":"41234@qq.com"})

        # 实例化对象传入的参数可以多，多的不会进行校验。但是绝不能少，少了is_valid()就会报False，而且key值也不能拼错
        form=UserForm(request.POST)

        if form.is_valid():
            # 如果表单字段验证成功，在form.cleaned_data中存储验证成功的字段key和value
            print(form.cleaned_data)
        else:
            # 如果验证失败，校验成功的字段依然会放存放在from.cleaned_data字典中
            print(form.cleaned_data)
            # 但是如果校验失败，校验失败的字段会存放在form.error中，存放的格式是字段key:错误信息
            # errors的数据类型是ErrorDict,{'name':[.......]}
            print(form.errors)

            # errors的key值是ErrorList类型
            print(form.errors.get('password'))
            print(form.errors.get('password')[0])

    return render(request,'register.html')