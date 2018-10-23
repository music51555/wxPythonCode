from views import *

# 路由控制器，将请求的路径和路径函数绑定在元祖中，用于遍历后访问函数
url_patterns = [
    ('/login', login),
    ('/favicon.ico', favicon),
    ('/index', index),
    ('/timer',timer)
]