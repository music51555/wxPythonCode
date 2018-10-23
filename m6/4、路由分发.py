from wsgiref.simple_server import make_server
from web_frame2.views import *

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/temples')])

    path = environ.get('PATH_INFO')

    # 路由控制器，将请求的路径和路径函数绑定在元祖中，用于遍历后访问函数
    url_patterns = [
        ('/login',login),
        ('/favicon.ico',favicon),
        ('/index',index)
    ]

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        # 最后返回给页面的数据，是在application函数中最后返回的，返回响应数据的时候，1、字节类型，2、存放在列表中
        return [func()]
    else:
        return [b'404']

httped = make_server('',8890,application)
httped.serve_forever()