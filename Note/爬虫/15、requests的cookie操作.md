`requests`的`cookie`操作



如果没有使用`session`对象发起个人主页的请求，会直接跳转至登录页面

```python
response = requests.get(url = site_url,headers = headers)
```



使用`session`对象发起请求，是因为如果请求发起成功后，将服务端设置的`cookie`信息存储到`session`对象中，使后续的请求都携带`session`信息

不仅`requests`可以`get`和`post`请求，`session`对象也可以发起`get`和`post`请求

```python
import requests

# 创建session对象
session = requests.session()

login_url = 'http://my.iciba.com/index.php?c=sso&m=web_login'
site_url = 'http://my.iciba.com/?c=user'

params = {
    'username': 'music51555',
    'password': 'nishi458',
    'remember': '0',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 通过session对象发起post请求，请求成功后，session对象中会自动存储响应体中的cookie信息，用于后续的请求
session.post(url = login_url, params = params, headers = headers)

# 继续发起个人主页的访问请求
response = session.get(url = site_url,headers = headers)

with open('self_site.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

