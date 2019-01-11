`scrapy`的发起`post`请求

第一种方法：

`yield scrapy.Request(url = url, callback=self.parse, method='post')`

第二种方法(**更推荐使用的方法**)：

` yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)`



**知识点1：**通过`yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)`发起`post`请求

**知识点2：**准备发起`post`请求前，要重写父类的`start_requests`方法，在其中循环遍历`url`，发起`post`请求

**知识点3：**`requests.post`发起的`post`请求是`data=xxx`，使用`scrapy`发起的`post`请求时`formdata=xxx`

**知识点4：**如果正常使用`scrapy`发起`get`请求，不用特意的使用`yield scrapy.Request(url=, callbakc=)`，因为在`parse`方法中已经得到了`start_urls`中网址的响应体

```python
# -*- coding: utf-8 -*-
import scrapy

class ScrapyDemoSpider(scrapy.Spider):
    name = 'scrapy_demo'

    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        data = {
            'kw': 'dog'
        }

        for url in self.start_urls:
            yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)

    def parse(self, response):
        print(response.text)
```



