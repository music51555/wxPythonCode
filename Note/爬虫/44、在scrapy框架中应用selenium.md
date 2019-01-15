在`scrapy`框架中应用`selenium`

**知识点1：**如果要实例化`selenium`中的浏览器驱动实例，可以在爬虫程序的`__init__`方法中实现

**知识点2：**爬虫程序父类`Spider`类提供了`closed`方法，在整个爬虫程序结束后运行，可以在其中编写`driver.close()`方法

**知识点3：**通过`xpath`获取当前标签对象的`class`属性，可以使用`./@class`

**知识点4：**当爬取页面的数据时动态加载时，在下载器下载页面后返回给爬虫程序前，经历了下载器的中间件`WangyiproDownloaderMiddleware`，在其中的`process_response`中可以拦截准备返回的响应体，做使用`selenium`重新请求的操作，且无论是`start_urls`中的请求还是二次发起的请求，都会经历该方法

**知识点5：**通过浏览器驱动的`driver.page_source`方法获取页面源码

**知识点6：**在一个标签对象下有多个`p`标签存放文本时，`xpath`可以写为`//div[@class=xxx]/p/text()`获取每一个`p`标签下的文本，通过`xpath().extract()`获取成一个列表结果，再次通过`''.join(列表)`得到一个字符串结果

**知识点7：**通过`from selenium import webdriver`导入包

```python
# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'

    start_urls = ['https://news.163.com/']

    tag_url = []

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='E:\workspace\wxPythonCode\wxPythonCode\m7\chromedriver_win32\chromedriver.exe')

    def closed(self, spider):
        self.driver.close()

    def parse(self, response):
        tag_list = response.xpath('//div[@class = "ns_area list"]/ul/li')
        for tag in tag_list:
            if tag.xpath('./@class').extract_first() in ['menu_guonei','menu_guoji','menu_hangkong']:
                url = tag.xpath('./a/@href').extract_first()
                self.tag_url.append(url)

        for url in self.tag_url:
            # 爬虫程序将起始start_urls交给scrapy引擎，引擎将所有的请求对象交付给调度器，在调度器中排入队列，依次交给下载器，下载器下载页面后，返回给爬虫程序，这时会经历下载器的中间件，由于新闻是动态加载的，所以此时没有加载出新闻，所以在中间件中借助selenium来实现拦截，重新请求页面，通过page_source方法获取页面源码，使用HtmlResponse封装后作为响应对象返回
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

        yield item

```



中间件`WangyiproDownloaderMiddleware`类

**知识点1：**由于所有通过下载器下载的页面都会经过中间件，所以需要`request.url`判断过滤对哪些`url`重新发起动态请求

**知识点2：**通过`driver.execute_script()`方法执行`js`脚本

**知识点3：**中间件类中的`spider`表示爬虫程序实例化的对象

**知识点4：**`driver.current_url`获取当前请求的`url`信息

**知识点5：**`from scrapy.http import HtmlResponse`类似`Django`的`HttpResponse`方法，当在中间件中准备返回页面源码时，就需要借助该方法了，`HtmlResponse(url = spider.driver.current_url, body = page_text, encoding = 'utf-8')`，封装为响应对象后返回

**知识点6：**下载器下载是依次返回下载页面的，所以会依次执行下载中间件，依次使用`selenium`重新发起请求

**知识点7：**`request`参数表示`scrapy`引擎交给调度器的请求对象，`request.url`表示当前请求的网址

**知识点8：**调用`window.scrollTo(0,document,body.scrollHeight)`方法加载底部动态数据后，需要停留几秒后在获取页面源码，否则无法加载出最新的源码

**知识点9：**`str.strip('  \n  \t')`中支持加入`\n、\t`等，针对性的去除空白数据

```python
from scrapy.http import HtmlResponse

class WangyiproDownloaderMiddleware(object):

    def process_response(self, request, response, spider):

        # 在调度器中不仅包含请求访问的4个版块的url，还包含start_urls中的请求地址，所以有针对性的拦截响应对象，获取页面源码，并通过HtmlResponse返回
        if request.url in ['http://news.163.com/domestic/', 'http://news.163.com/world/', 'http://war.163.com/', 'http://news.163.com/air/']:
            # 在process_response中是在下载器下载页面后将response响应对象返回爬虫程序前执行的，但是没有加载出动态的新闻数据，所以通过selenium重新发起请求，获取页面源码，包含了动态加载的数据
            spider.driver.get(request.url)
            time.sleep(5)

            # 执行js脚本后下拉滚动条，等待5秒后，再获取页面源码
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.driver.execute_script(js)
            time.sleep(5)

            page_text = spider.driver.page_source

            response = HtmlResponse(url = spider.driver.current_url, body = page_text, encoding='utf-8')

            # 此时返回的response是返回给tag_detail方法中的response
            return response
		# 如果请求对象的url不在指定集合中，那么直接返回response响应对象
        else:
            return response
```







本节是针对`RedisSpider`实现的分布式爬虫程序

UA池

代理池



先编写Spider类型的爬虫，再调整为RedisSpider类型的爬虫程序





在def __init__中初始化driver

在def closed是spider类中的方法，重写关闭driver.quit()

在settings.py中开启中间件

request对应的是请求对象，response对应的是响应对象，spider对应爬虫程序对应的类的实例对象，可以在中间件中先打印响应对象

在process_response下载中间件方法中，拦截到了请求二次页面的的response响应体，通过request.url判断是否在二次请求的url集合中，如果在则返回HtmlResponse

from scrapy.http import HtmlResponse

return HtmlResponse(url = request.current_url, body = 通过page_source获取到的页面内容， encoding = 'utf-8', request = request)

如果不在则还是返回response





在中间件中通过driver对象发起的二级页面请求，是包含动态加载的数据



此时返回的内容会返回给二次页面请求的callback回调函数中的response



strip("\n \t  ")





