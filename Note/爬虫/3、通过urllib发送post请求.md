`XHR`表示抓取基于`Ajax`的请求



**知识点1：**如果要发送`post`请求，必须为请求准备参数字典

**知识点2：**将字典内容通过`urlencode`方法，变为字符串类型

**知识点3：**发送请求中的数据必须为`bytes`类型，所以调用`str.encode()`方法

**知识点4：**无论发送`get`还是`post`请求，都调用`urllib.request.urlopen`方法，有data参数就是`post`请求

```python
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

# 如果要发送post请求，必须为post设置参数，get请求之所以不用设置参数，是因为get请求的参数在url中
data = {
    'kw': '西瓜'
}

# 对post请求中的字典数据进行编码，转换为非ASCII码的值kw=%E8%A5%BF%E7%93%9C，如果是get请求中的字符编码，调用urllib.parse.quote方法，类型时str类型
data = urllib.parse.urlencode(data)

# 因为通过urllib.parse.urlencode()得到的结果是字符串str类型，所以需要将其转换为bytes类型
data = data.encode()

# 无论发送get还是post请求，都调用urllib.request.urlopen方法
response = urllib.request.urlopen(url = url, data = data)

data = response.read()

with open('fanyi.json', 'wb') as f:
    f.write(data)
```

