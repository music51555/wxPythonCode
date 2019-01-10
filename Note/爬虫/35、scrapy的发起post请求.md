`scrapy`的发起`post`请求

第一种方法：

`yield scrapy.Request(url = url, callback=self.parse, method='post')`

第二种方法(**更推荐使用的方法**)：

` yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)`



**知识点1：**通过`yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)`发起post请求

**知识点2：**准备发起post请求前，要重写父类的`start_requests`方法，循环遍历`url`，发起`post`请求

**知识点3：**`requests.post`发起的`post`请求是`data=xxx`，使用`scrapy`发起的`post`请求时`formdata=xxx`

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



