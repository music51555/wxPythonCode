from django.shortcuts import render,HttpResponse
from PIL import Image,ImageDraw,ImageFont
import random
import os
from io import BytesIO
import string

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
valid_img_bgc=os.path.join(BASE_DIR,'static','valid_img_bgc','valid_bgc.png')

def login(request):

    return render(request,'login.html')

def get_validCode_img(request):
    def get_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img=Image.new('RGB',(270,40),color=get_color())

    # 表示通过ImageDraw画笔，画在哪个图片上
    draw=ImageDraw.Draw(img)

    # 根据ttf字体文件创建字体对象，并设置字体大小
    fzxzt_font=ImageFont.truetype('static/font/KumoFont.ttf',size=30)

    for i in range(5):
        rand_str = ''.join(random.sample(string.ascii_letters + str(random.randint(0, 9)), 1))
        # 在图片上可以写字，可以划线，可以写点，分别传入(坐标，字符，文字颜色，字体对象)
        draw.text((i*60,3),rand_str,fill=get_color(),font=fzxzt_font)

    f=BytesIO()
    img.save(f,'png')
    data=f.getvalue()

    return HttpResponse(data)