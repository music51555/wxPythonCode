import datetime

# 视图函数
def login():
    with open('../html/login.html','rb') as f:
        fdata = f.read()
    return fdata

def favicon():
    with open('../images/favicon.ico','rb') as f:
        fdata = f.read()
    return fdata

def index():
    with open('../html/index.html','rb') as f:
        fdata = f.read()
    return fdata

def timer():

    now = datetime.datetime.now().strftime('%Y-%m-%d %X')
    return now.encode('utf-8')