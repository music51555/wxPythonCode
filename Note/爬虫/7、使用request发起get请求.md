#### **使用`request`发起`get`请求**

**知识点1**：调用`request.get`发起get请求

**知识点2**：通过`response.text`获取网页文本

```python
import requests

url = 'https://www.baidu.com'

response = requests.get(url)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```



**`response`的一些属性：**

#### `response.content`

得到二进制`bytes`类型的网页内容

```
b'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css><title>\xe7\x99\xbe\xe5\xba\xa6\xe4\xb8\x80\xe4\xb8\x8b\xef\xbc\x8c\xe4\xbd\xa0\xe5\xb0\xb1\xe7\...
```



#### `response.status_code`

请求状态码

```
200
```



#### `response.headers`

获取响应头信息

```
{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Sat, 29 Dec 2018 06:54:51 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:56 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
```



#### `response.url`

获取请求的`url`

```
https://www.baidu.com/
```



#### 使用`request`发起带参数的`get`请求

发起`get`请求后，`url`直接写为带参数的`get`请求即可

```python
import requests

url = 'https://www.sogou.com/web?query=可口可乐&ie=utf8'

response = requests.get(url)

print(response.text)

with open('zhou.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

