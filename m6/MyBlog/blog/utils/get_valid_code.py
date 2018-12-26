import random
from PIL import Image,ImageDraw,ImageFont
import string
from io import BytesIO


def get_valid_code_img(request):
    def get_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    img = Image.new('RGB', (270, 40), color=get_color())

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('static/font/KumoFont.ttf', size=30)

    valid_code = ''
    for i in range(5):
        rand_str = ''.join(random.sample(string.ascii_letters + str(random.randint(0, 9)), 1))

        # 每次生成的一个随机字符串，拼接一个完整的5位随即验证码
        valid_code += rand_str

        # 在图片上可以写字，可以划线，可以写点，分别传入(坐标，字符，文字颜色，字体对象)
        draw.text((i*60, 10), rand_str, fill=get_color(), font=font)

    # 用户访问login页面所生成的验证码，被存储在当前会话的session中，供在login视图函数中验证正确与否使用
    request.session['valid_code'] = valid_code

    width = 270
    height = 40

    for i in range(10):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)

        draw.line((x1, x2, y1, y2), fill=get_color())

    for i in range(100):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_color())
        x = random.randint(0, width)
        y = random.randint(0, height)

        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_color())

    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()

    return data
