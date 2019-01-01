urllib模块：使用频率低

模拟浏览器发送请求，包含request和parse子模块

**执行的流程：**

指定URL

发起请求

返回响应体

持久化存储



```python
import urllib.request

url = 'https://www.sogou.com/'

response = urllib.request.urlopen(url = url)

data = response.read()

with open('./sogou.html', 'wb') as f:
    f.write(data)
    print('写入数据成功')
```





requests模块：使用频率高