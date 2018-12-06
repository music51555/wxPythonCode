from django.shortcuts import render,HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random
import os
from io import BytesIO
import string
from django.http import JsonResponse
from django.contrib import auth

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
valid_img_bgc=os.path.join(BASE_DIR,'static','valid_img_bgc','valid_bgc.png')

def login(request):

    response={'user':None,'msg':None}

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        valid_code=request.POST.get('valid_code')

        if valid_code.lower()==request.session['valid_code'].lower():
            # 通过auth.authenticate来验证用户名和密码是否正确，如果校验正确则返回的对象为当前用户的用户名alex，如果错误则为None
            user=auth.authenticate(username=username,password=password)
            if user:
                # ajax提交的请求如果校验正确，不要想着return一个跳转页面，因为在ajax的success函数中接收的是一个data字段，如果校验正确，在ajax中通过location.href='/index'来跳转
                auth.login(request,user)
                response['user']=username
            else:
                response['msg']='username or password error'

            return JsonResponse(response)
        else:
            response['msg']='valid_code error'

            return JsonResponse(response)

    return render(request,'login.html')

def index(request):

    return render(request,'index.html',locals())

def get_validCode_img(request):
    def get_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img=Image.new('RGB',(270,40),color=get_color())

    # 表示通过ImageDraw画笔，画在哪个图片上
    draw=ImageDraw.Draw(img)

    # 根据ttf字体文件创建字体对象，并设置字体大小
    fzxzt_font=ImageFont.truetype('static/font/KumoFont.ttf',size=30)

    valid_code=''
    for i in range(5):
        rand_str = ''.join(random.sample(string.ascii_letters + str(random.randint(0, 9)), 1))
        # 每次生成的一个随机字符串，拼接一个完整的5位随即验证码
        valid_code+=rand_str

        # 在图片上可以写字，可以划线，可以写点，分别传入(坐标，字符，文字颜色，字体对象)
        draw.text((i * 60, 3), rand_str, fill=get_color(), font=fzxzt_font)

    # 用户访问login页面所生成的验证码，被存储在当前会话的session中，供在login视图函数中验证正确与否使用
    request.session['valid_code']=valid_code

    width = 270
    height = 40

    for i in range(10):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)

        draw.line((x1, x2, y1, y2), fill = get_color())

    for i in range(100):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_color())
        x = random.randint(0, width)
        y = random.randint(0, height)

        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_color())

    f=BytesIO()
    img.save(f,'png')
    data=f.getvalue()

    return HttpResponse(data)