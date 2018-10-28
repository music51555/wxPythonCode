视图函数

request，封装请求数据

```python
#请求方式，打印GET或POST
request.method
```

```html
<!--点击form表单的提交按钮，如果没有在setting.py中注释csrf，那么会显示forbidden-->
forbidden：防跨域请求的安全机制

<!--如果action没有写，则是以当前页面路径为准-->
<form action='' method="post">

<!--如果只写'/index/'，那么会以当前域名+端口拼接路径,http://127.0.0.1:8000/index/-->
<form action='/index/' method="post">
```

```python
#get请求会将参数附加在URL中，URL?name=alex&age=2，request.GET.get()获取字典的key值
request.GET.get()

#post请求是在报文中的，get字典的key获取字典的value，但value不是一个列表
request.POST.get()
```

```python
#什么是路径
#url = 协议(http://)+IP:port/路径(index/2003)?get请求的参数
request.path

#根目录/，指定视图函数
re_path(r'^$',view.index)

#request.path表示只打印路径，request.get_full_path表示打印路径和get请求参数
request.get_full_path()
```

```python
#字符串，表示提交的数据的编码方式（如果为 None 则表示使用 DEFAULT_CHARSET 的设置，默认为 'utf-8'），可写属性，使用用户设置编码通过GET和POST方法请求数据
request.encoding
```

```python
#python字典，包含所有HTTP的请求头
request.META
```

```python
#python字典，包含所有的cookie。键和值都为字符串
request.COOKIES
```

```python
#判断是否是ajax请求
request.is_ajax()
```

