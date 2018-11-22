**无状态保存：**在客户端发送请求到服务器时，每一次请求服务器都认为这是一次新的请求，不知道客户端之前发送过哪些请求，这是无状态保存

**cookie：一个浏览器**针对**一个服务器**存储的key-value

客户端发送请求后，`cookie`是存储在请求头中发送至服务器的，如`login`操作，如果登录成功，服务器会设置`cookie`信息，设置`cookie`字典，如`{'login':True}`，返回时将`cookie`信息存储在响应体中返回浏览器，下一次浏览器再次发送请求时，cookie信息中会存储着`{'login':True}`

**特点：**

1、cookie是存储在磁盘上的，建立cookie后，以后对该服务器的每一次请求都会带着cookie，不管开机关机

2、cookie的有效期是2周，可以设置，cookie失效后就不会被附加在请求中了

3、每个浏览器之间的cookie是独立的

4、访问其他服务器时，不会带着访问其他服务器的cookie信息



响应体：

```python
# 所有的响应体在源码中都是基于HttpResponse的
return HttpResponse()
return render()
return redirect()
```

cookie是由服务器设置的，是由服务器的响应体设置的

```
respone=HttpResponse('xx')
respone=render(xxx)
respone=redirect()
respone.setCookie
```

每一次请求时，cookie是存放在请求头request中的

request.COOKIE.get('login')



hi,yuan