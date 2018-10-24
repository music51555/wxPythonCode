import sys,os
from wsgiref.simple_server import make_server

sys.path.append(os.path.dirname(__file__))
from urls import url_patterns

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html,charset=utf-8')])
    print(environ)
    path = environ.get('PATH_INFO')

    func = None
    for item in url_patterns:
        if path == item[0]:
            func = item[1]
            break

    if func:
        # 最后返回给页面的数据，是在application函数中最后返回的，返回响应数据的时候，1、字节类型，2、存放在列表中
        return [func(environ)]
    else:
        return [b'404']

httped = make_server('',8890,application)
httped.serve_forever()