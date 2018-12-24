#### web框架

开发框架，用来支持动态网站、网络应用和网络服务的开发

#### WSGI协议

Web Server Gateway Interface：web应用程序、web服务、web框架之间的一种接口 ，接收HTTP请求，解析HTTP请求，发送HTTP请求

#### wsgiref模块

python基于wsgi协议开发的服务模块 ，可以解析HTTP请求，可以封装HTTP响应

```python
from wsgiref.simple_server import make_server

def application(environ,start_response):
    # environ参数，按照http协议解析数据，封装为字典形式，存储的是HTTP请求报头
    # 在其中可以找到'REQUEST_METHOD': 'GET', 'PATH_INFO': '/'等信息
    print(environ)
    path = environ.get('PATH_INFO')

    # 在start_response中封装了响应首行和响应头，在此处设置的404状态，是在浏览器的network中请求链接中显示的
    start_response('200 OK', [('Content-Type', 'text/html')])
	
    # 同时判断了请求的路径和其他情况，其他情况是favicon.ico图标请求，如果不增加其他判断会报错
    if path == '/login':
        with open(temples, 'rb') as f:
            fdata = f.read()
    else:
        with open(temples,'rb') as f:
            fdata = f.read()
    # 在return中返回字节响应体
    return [fdata]

#封装了socket，省去了创建socket对象，socket.bind，socket.listen等
httped = make_server("127.0.0.1",8801,application)

# 监听HTTP请求，等待用户连接，一旦有用户连接，则调用application回调函数，在调用时会传递两个参数environ和start_response
# 在该方法中将所有的http请求解析成了字典形式，全部放在environ参数中
httped.serve_forever()
```