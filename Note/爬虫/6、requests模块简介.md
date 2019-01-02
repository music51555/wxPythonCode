`requests`模块

`python`原生的基于网络请求的模块，模拟浏览器发起请求



**对比于`urllib`:**

手动处理非`ASCII`字符，如`urllib.parse.quote('周杰伦')`

手动处理`post`请求的参数，将数据添加到字典中，并通过`urllib.parse.urlencode()`转换为字符串，再通过`encode()`转换为`bytes`类型

`cookie`的代理操作繁琐，创建`cookiejar`对象，创建`handler`对象，创建`opener`对象



**安装`requests**

`pip3 install requests`