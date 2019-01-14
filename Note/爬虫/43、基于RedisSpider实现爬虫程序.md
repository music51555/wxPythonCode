##### 抓取指定页面时使用

##### 基于`scrapy.Spider`实现抓取`start_urls`中页面数据的爬虫程序：

1、通过`scrapy genspider baidu www.baidu.com`创建爬虫程序

3、在`parse`方法中得到`start_urls`网页的响应对象`response`，并通过`xpath`方法解析页面数据

4、在`items.py`中定义变量

5、引入`items`中的类进行实例化，封装变量，`yield item`

6、在项目的`pipeline`中，解析`item`对象得到变量，并进行持久化存储



#####　抓取页面的二级页面时使用

##### 基于`scrapy.Spider`实现发起`get`和`post`请求的爬虫程序

1、通过`yield scrapy.Request(url = xxx, callback= xxx，meta={'item:item'})`实现发起`get`请求，指定`callback`函数解析页面数据，并传递`item`对象

2、通过`yield scrapy.FormRequest(url = xxx, formdata = xxx, callback = xxx)`发起`post`请求

3、通过重写`scrapy.Spider`父类中的`start_requests`方法，定义`post`请求内容的字典后，循环`start_urls`来发起`post`请求



##### 基于`CrawSpider`实现通过`link`和`rule`按正则匹配多页链接的爬虫程序：

1、创建爬虫程序`scrapy genspider -t crawl baidu www.baidu.com`

2、定义链接提取器`link`

3、定义规则提取器`rule`

4、解析页面数据`parse`



##### 基于`RedisCrawlSpider`实现了按`redis`的`scheduler、filter、pipeline`实现的分布式爬虫程序，实现在多台机器部署代码，一同抓取数据

0、`pip3 install scrapy_redis`

1、引入`from scrapy_redis.spiders import RedisCrawlSpider`

2、继承引入的父类`RedisCrawlSpider`

3、设置`redis_key`，用于在`redis`数据库中存放爬取到的数据

4、`link`链接提取器，通过正则表达式匹配网页中的`URL`

5、`rule`规则提取器，对匹配到的`URL`发起请求，执行指定函数，以及通过`follow`参数设置是否应用于新网页

6、在`parse_item`方法中解析响应对象中的网站数据

7、在`settings.py`中配置使用`redis`的`pipeline`管道文件

8、在`settings.p`y中配置使用`redis`的调度器`SCHEDULER`、去重器`Filter`

9、在`settings.py`中配置`redis`数据库连接信息，`HOST`和`PORT`

7、在`parse_item`中`yield item`，此时是将`item`返回到`redis`的`pipeline`中

8、通过``scrapy runspider xxx.py`运行爬虫程序，程序开始监听`redis`数据库

9、在`redis`中`lpush redis_key 爬取的网址`

10、程序开始爬取，并在`lrange redis_key 0 -1`中查询爬取到的数据



本节是针对`RedisSpider`实现的分布式爬虫程序

UA池

代理池



先编写Spider类型的爬虫，再调整为RedisSpider类型的爬虫程序

extract_first提取xpath结果列表中，每一个selector中的data值

extract提取xpath结果列表中，每一元素的所有内容

爬取国际、国内、军事、航空二级页面的数据，并抓取标题、缩略图urk、tag，但是没有抓取到，是因为没有加载出动态加载出的内容，所以借助selenium来实现，

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















































