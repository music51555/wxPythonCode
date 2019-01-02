通过`urllib.parse.quote`解析非`ASCII`字符



`quote`：美 /kwot/ 引用



`url`中不能存在非`ASCII`码的字符数据，如可口可乐，所以需要使用`urllib.parse.quote`进行转码

```python
import urllib.request
import urllib.parse

# 通过urllib.parse.quote引用非ASCII字符
word = urllib.parse.quote('可口可乐')

# 连接url和引用字符
url = 'https://www.sogou.com/web?query=' + word

response = urllib.request.urlopen(url)

data = response.read()

with open('rmb.html', 'wb') as f:
    f.write(data)
```



```python
import urllib

url = 'https://fanyi.baidu.com/sug'

data = urllib.parse.urlencode([
    ('kw','西瓜')
])

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

request = urllib.request.Request(url,data=data.encode(), headers = headers)

# request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')

response = urllib.request.urlopen(request)

print(response.read())
```

