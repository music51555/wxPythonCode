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
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    img=Image.new('RGB',(270,40),color=get_color())

    draw=ImageDraw.Draw(img)

    font=ImageFont.truetype('static/font/KumoFont.ttf',size=30)

    for i in range(5):
        rand_str=''.join(random.sample(string.ascii_letters+str(random.randint(0,9)),1))
        print(rand_str)
        draw.text((i*50,5),rand_str,fill=get_color(),font=font)

    f=BytesIO()
    img.save(f,'png')
    data=f.getvalue()

    return HttpResponse(data)