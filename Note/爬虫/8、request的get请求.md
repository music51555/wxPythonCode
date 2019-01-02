`request`的`get`请求

##### 1、直接写在url中自动解析参数

无论是`url`还是带参数的`url`都可以直接写为`url+参数`的形式

```python
import requests

url='https://www.sogou.com/web?query=周杰伦&ie=utf8'

response = requests.get(url)

print(response.text)
```



##### 2、将参数写在params中

`requests`的get请求中可以包含`url`参数，还可以包含`params`参数

```python
import requests

url='https://www.sogou.com/web'

params = {
    'query': '周杰伦',
    'ie': 'urf8'
}

response = requests.get(url = url, params = params)

print(response.text)
```



#####  3、`request`的`get`请求封装请求头信息

`get`请求不仅包含`url`和`params`参数，还包含`headers`参数，封装字典形式的`headers`请求头

```python
import requests

url='https://www.sogou.com/web'

params = {
    'query': '周杰伦',
    'ie': 'urf8'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get(url = url, params = params, headers = headers)

print(response.text)
```

