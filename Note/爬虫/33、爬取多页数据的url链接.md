爬取多页数据的`url`链接

**知识点1：**使用`response.xpath`方法获取糗百中的糗事时，如果糗事有多行，只能获取到一行文本，使用`BeautifulSoup`模块解决该问题

**知识点2：**如果想获取`ul`下`li`标签的最后一个，不要使用如`nth-of-type()`和不支持的`last-child()`方法，直接获取所有的`li`标签，返回的是列表数据，通过`['-1']`取得最后一个

**知识点3：**通过`soup.a['href']`得到标签对象的属性值

**知识点4：**通过`yield scrapy.Request(url=,callback=)`方法执行`get`请求，并执行当前回调函数

```python
# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from .. import items

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'

    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        qiushi_list = soup.select('#content-left > div')
        next = soup.select('.next')

        for qiushi in qiushi_list:
            author = qiushi.select('.author h2')[0].text
            content = qiushi.select('.content > span')[0].text

            item = items.QiubaiPagesItem()
            item['author'] = author
            item['content'] = content

            yield item

        if next:
            next_url = 'https://www.qiushibaike.com' + soup.select('.pagination li a')[-1]['href']
            yield scrapy.Request(url = next_url, callback=self.parse)
```

