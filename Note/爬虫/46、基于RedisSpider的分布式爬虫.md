基于`RedisSpider`的分布式爬虫

**知识点1：**基于`RedisSpider`的分布式爬虫是在`Spider`爬虫的基础之上修改的代码，所以先编写普通的`Spider`爬虫代码即可

**知识点2：**如果想修改为分布式的`RedisSpider`爬虫程序，需要先从`from scrapy_redis.spiders import RedisSpider`，然后使爬虫程序继承于这个父类

**知识点3：**如果想修改为分布式的`RedisSpider`爬虫程序，分别需要配置`redis.conf`和项目的`settings.py`文件的调度、`pipeline、redis`数据库连接信息等

**知识点4：**如果创建时`def __init__`方法，在其中要编写`super(WangyiSpider,self).__init__()`

**知识点5：**使用`redis_key`代替`start_urls`

**知识点6：**在爬虫程序的最后要`yield item`，将他返回给`pipeline`文件

**知识点7：**启动程序后开始监听爬虫网址，在`redis`中通过`lpush`和`lrange`输入网址和读取结果

```python
# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from selenium import webdriver
from scrapy_redis.spiders import RedisSpider

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import WangyiproItem

class WangyiSpider(RedisSpider):
    name = 'wangyi'

    redis_key = 'wangyi'

    tag_url = []

    def __init__(self):
        super(WangyiSpider,self).__init__()
        self.driver = webdriver.Chrome(executable_path='E:\workspace\wxPythonCode\wxPythonCode\m7\chromedriver_win32\chromedriver.exe')

    def parse(self, response):
        tag_list = response.xpath('//div[@class = "ns_area list"]/ul/li')
        for tag in tag_list:
            if tag.xpath('./@class').extract_first() in ['menu_guonei','menu_guoji','menu_hangkong']:
                url = tag.xpath('./a/@href').extract_first()
                self.tag_url.append(url)

        for url in self.tag_url:
            # 爬虫程序将起始start_urls交给scrapy引擎，引擎将所有的请求对象交付给调度器，在调度器中排入队列，一次交给下载器，下载器下载页面后，返回给爬虫程序，这时会经历下载器的中间件，由于新闻是动态加载的，所以此时没有加载出新闻，所以在中间件中借助selenium来实现拦截，重新请求页面，通过page_source方法获取页面源码，使用HtmlResponse封装后作为响应对象返回
            yield scrapy.Request(url = url, callback=self.tag_detail)

    def tag_detail(self, response):
        # parse方法中请求版块的详情页后，得到结果的长度为0，没有获取到任何新闻内容，这是因为在进入新闻详情页时，新闻是动态加载出来的，所以需要借助selenium配合使用
        news_list = response.xpath('//div[@class = "data_row news_article clearfix "]')

        for news in news_list:
            news_title = news.xpath('.//div[@class = "news_title"]/h3/a/text()').extract_first()
            news_url = news.xpath('.//div[@class = "news_title"]/h3/a/@href').extract_first()
            # 得到标签下的所有文本，那么就不能使用extract_first()方法了，因为有多个值，所有适用extract()方法，得到的是一个列表，通过','.join方法连接列表中的每一个元素
            news_tag = ','.join(news.xpath('.//div[@class = "keywords"]//text()').extract())
            update_time = news.xpath('.//span[@class = "time"]/text()').extract_first()
            img_url = news.xpath('//a[@class = "na_pic"]/img/@src').extract_first()

            item = WangyiproItem()
            item['news_title'] = news_title
            item['news_tag'] = news_tag
            item['update_time'] = update_time
            item['img_url'] = img_url

            yield scrapy.Request(url = news_url, callback=self.getContent, meta = {'item':item})

    def getContent(self, response):
        # 文章内容是存在于post_text标签类下的每一个p标签，所以获取每一个p标签下的文本内容，得到的是一内容列表
        content = response.xpath('//div[@class = "post_text"]/p/text()').extract()
        item = response.meta['item']
        item['content'] = content

        print(content)

        yield item

```