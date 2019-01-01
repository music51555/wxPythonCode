urllib的

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

