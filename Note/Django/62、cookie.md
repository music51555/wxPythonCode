**无状态保存：**在客户端发送请求到服务器时，每一次请求服务器都认为这是一次新的请求，不知道客户端之前发送过哪些请求，这是无状态保存

**cookie：一个浏览器**针对**一个服务器**存储的key-value

**设置cookie的过程：**

客户端发送请求后，`cookie`是存储在请求头中发送至服务器的，第一次请求时是空的`{ }`，如`login`操作，如果登录成功，服务器会设置`cookie`信息，设置`cookie`字典，如`{'login':True}`，存储在响应体中返回浏览器，下一次浏览器再次发送请求时，cookie信息中会存储着`{'login':True}`

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



cookie的大小上限4KB

一个服务器最多在浏览器客户端保存20个cookie

一个浏览器最多保存300个cookie