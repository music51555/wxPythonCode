Django中间件



在`settings.py`中有中间件的配置文件：

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

引入每一个中间件，查看内容：

包含`process_request`和`process_response`方法

```python
from django.middleware.security import SecurityMiddleware

class SecurityMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        pass
	
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        pass
```



**中间件的工作过程：**

客户端发送请求后，首先由`wsgiref`解析客户端请求的数据，解析为`request`对象，然后依次执行每一个中间件的`process_request`，到达路由分发的`url.py`，执行视图函数后返回响应体，再次经过中间件，依次执行每一个中间件的`process_response`，回到`wsgiref`中，封装响应体（包含响应首行、响应体），发送会浏览器客户端解析为`HTML`页面