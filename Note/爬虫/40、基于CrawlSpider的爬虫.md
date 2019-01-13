爬虫程序的父类是`Spider`

`CrawlSpider`是`Spider`的一个子类，包含链接提取器、规则解析器，当要提取多页内容时使用

**创建爬虫程序：**

`scrapy genspider -t crawl chouti dig.chouti.com`



初步的`CrawlSpider`程序：

**知识点1：**实例化**链接提取器**`link`对象，通过传入的正则表达式在页面中匹配数据

**知识点2：**实例化**规则解析器**对象,将链接提取器`link`对象传入规则解析器，对收集的所有连接发起请求，调用`parse_item`回调函数，返回页面的响应对象

**知识点3：`follow`**表示是否在新的页面中继续应用链接提取器的中的正则表达式提取链接数据

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    start_urls = ['http://dig.chouti.com/']

    # 实例化链接提取器对象，通过传入的正则表达式在页面中匹配数据，提取器将得到的
    link = LinkExtractor(allow=r'/all/hot/recent/\d+')

    # 实例化规则解析器对象,将链接提取器link对象传入规则解析器，对收集的所有连接发起请求，调用parse_item回调函数，返回页面的响应对象，follow表示是否在新的页面中继续应用链接提取器的中的正则表达式提取链接数据
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
```

运行程序得到：

在每一页通过正则表达式匹配到了链接地址，`rules`对象对其发起请求，调用`callback`回调函数得到请求响应对象，在其中进行数据解析

```shell
<200 https://dig.chouti.com/all/hot/recent/1>
<200 https://dig.chouti.com/all/hot/recent/9>
<200 https://dig.chouti.com/all/hot/recent/7>
<200 https://dig.chouti.com/all/hot/recent/10>
<200 https://dig.chouti.com/all/hot/recent/4>
<200 https://dig.chouti.com/all/hot/recent/3>
<200 https://dig.chouti.com/all/hot/recent/8>
<200 https://dig.chouti.com/all/hot/recent/5>
<200 https://dig.chouti.com/all/hot/recent/6>
<200 https://dig.chouti.com/all/hot/recent/2>
<200 https://dig.chouti.com/all/hot/recent/13>
<200 https://dig.chouti.com/all/hot/recent/11>
<200 https://dig.chouti.com/all/hot/recent/12>
<200 https://dig.chouti.com/all/hot/recent/14>
<200 https://dig.chouti.com/all/hot/recent/16>
<200 https://dig.chouti.com/all/hot/recent/15>
<200 https://dig.chouti.com/all/hot/recent/18>
```



**应用实例：**

根据分页空间的url链接，使用正则表达式匹配，获取每一页的帖子标题

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    # allowed_domains = ['www.chouti.com']
    start_urls = ['https://dig.chouti.com/']

    link = LinkExtractor(allow=r'/all/hot/recent/\d+')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//a[@class = "show-content color-chag"]/text()').extract_first().strip()
        print(title)
```