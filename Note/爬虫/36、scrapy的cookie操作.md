`scrapy`的`cookie`操作

**知识点1：**`scrapy`发起`post`请求后，再次发起`get`请求，此次请求中是携带`cookie`信息的，所以可以不做任何`cookie`设置直接访问个人主页

```python
# -*- coding: utf-8 -*-
import scrapy

class ScrapyDemoSpider(scrapy.Spider):
    name = 'scrapy_demo'

    start_urls = ['https://www.douban.com/accounts/login']

    def start_requests(self):
        data = {
            'ource': 'index_nav',
            'form_email': '18611848257',
            'form_password': 'nishi458_2'
        }

        for url in self.start_urls:
            yield scrapy.FormRequest(url = url, formdata = data, callback=self.parse)

    def self_page_parse(self, response):
        with open('self_page.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

    def parse(self, response):
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        self_page = 'https://www.douban.com/people/143360064/'

        yield scrapy.Request(url = self_page, callback=self.self_page_parse )
```

