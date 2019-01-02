基于`requests`模块的代理

**什么是代理：**

第三方代理代替本体执行相关操作



**为什么用代理：**

访问次数过多导致`IP`被封



**代理的分类：**

**正向代理：**代理客户端获取数据

免费代理`IP`：

```
1、www.goubanjia.com
2、快代理
3、西祠代理
```

**反向代理：**代理服务端提供数据



**知识点1：**通过字典封装代理信息，`key`值的协议要和`url`中的协议相匹配

**知识点2：**通过`proxies`参数传入代理信息

```python
import requests

url = 'http://www.baidu.com/s?'

params = {
    'ie': 'utf-8',
    'wd': 'ip',
}

# 封装代理信息，其中的http要和url中的协议相匹配
proxy = {
    'http': '112.217.199.122:55872'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 通过proxies参数传入代理信息
response = requests.get(url = url, params=params, proxies = proxy, headers = headers)

with open('ip.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
```

