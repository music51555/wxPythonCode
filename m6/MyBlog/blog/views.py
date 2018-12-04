from django.shortcuts import render,HttpResponse

def login(request):

    return render(request,'login.html')

def get_validCode_img(request):

    # 对于验证码图片，直接打开一张图片返回，这并不合适，因为图片是固定的
    # with open('lufei.jpeg','rb') as f:
    #     data=f.read()
    import random
    def get_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    from PIL import Image
    img=Image.new('RGB',(270,40),color=get_color())

    with open('ValidCode_bgc.png','wb') as f:
        img.save(f,'png')

    with open('ValidCode_bgc.png','rb') as f:
        data=f.read()

    return HttpResponse(data)