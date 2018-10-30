#### 什么是HTTP协议

Hyper Text Transfer Protocol**超文本传输协议**，基于TCP/IP的应用层协议，就是服务端与客户端传输超文本标记语言HTML的协议，由客户端发送请求，服务端响应请求

HTTP协议是无状态的协议，即不会保存用户的状态，如登录状态，引入Cookie技术后，实现了状态管理



#### HTTP请求格式

![http请求格式](./images/http请求格式.png)



**请求首行：**

```python
方法        URL         协议版本

GET         /          HTTP/1.1\r\n
POST        /          HTTP/1.1\r\n

1、参数位置
get请求时，参数会在URL中展示，以?分隔，参数间以&连接，查询操作时多用get请求
www.baidu.com?name=alex&age=22

post请求时，参数会在请求报头中的请求体中展示，也就是服务器通过data = conn.recv(1024)接收，在/r/n/r/n后展示，修改、提交、更新时多用post请求
\r\n\r\nusername=wangxin&pwd=123456'

2、URL长度
get有限制
post没有限制

在IE8下的URL地址总长度为：4076，超过该长度会自动忽略后面的内容；
在firefox 25下的URL地址总长度可以达到:7530，超过该长度会访问错误；
在chrome 29.0.1547.62 的最大总长度达到:7675，超过该长度会访问错误；
```

**请求头：**

键值对的形式展示

```python
Host: 
#请求的服务端名称
Connection：
#close，请求-应答模式，连接后立即断开
#keep-alive：使客户端与服务端的连接持久有效，当客户端出现后继的请求时，无需重新建立连接。性能更高，避免了重新建立/释放连接的开销
Connect-Type：
#数据类型
Connect-Length：16 
#客户端发送数据的字节长度，如name=alex&age=22，16的字节
```

**请求体：**

```python
#客户端发送的请求参数
name=alex&age=22
```



**get请求报文：**

```python
GET / HTTP/1.1\r\n
Host: 127.0.0.1:8800\r\n
Connection: keep-alive\r\n
Cache-Control: max-age=0\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36\r\n
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\n
```



**post请求报文：**

客户端发送请求后，服务端接收到的请求内容。请求头参数以/r/n分隔，请求头和请求体以/r/n/r/n分隔

```python
POST / HTTP/1.1\r\n
Host: 127.0.0.1:8800\r\n
Connection: keep-alive\r\n
Content-Length: 27\r\n
Cache-Control: max-age=0\r\n
Origin: http://127.0.0.1:8800\r\n
Upgrade-Insecure-Requests: 1\r\n
Content-Type: application/x-www-form-urlencoded\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36\r\n
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
Referer: http://127.0.0.1:8800/\r\n
Accept-Encoding: gzip, deflate, br\r\n
Accept-Language: zh-CN,zh;q=0.9\r\n\r\
nusername=wangxin&pwd=123456
```



#### HTTP响应格式

![http响应格式](.\images\http响应格式.png)

分为响应首行、响应头和响应体



必须按照响应格式发送响应**“HTTP1.1 200 OK”**

```python
#如果没有按照既定的格式发送响应，那么浏览器会提示“127.0.0.1 发送的响应无效”
conn.send((b'HTTP1.1 200 OK\r\n\r\n')+fdata)
```



响应头可有可无

```python
#其中Content-type:text/html响应头可有可无
conn.send((temples)+fdata)
```

添加响应头后，在浏览器接收到响应后，会显示添加的响应头

![http响应头](.\images\http响应头.png)





**响应状态码：**

1开头，接收的请求正在处理

2开头，请求正常处理完毕

3开头，重定向：服务端响应访问域名不存在，让浏览器客户端重新发送一个请求，指向新的域名，重新定向到新的域名上访问

4开头，请求的资源不存在

5开头，服务器内部错误，处理请求出错