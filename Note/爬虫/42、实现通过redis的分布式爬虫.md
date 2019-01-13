##### 概述：

分布式爬虫程序，是借助`redis`数据库完成的，我们可以将代码部署到多台服务器上，运行程序后，同时开始监听`redis`数据库，当在`redis_key`中`lpush`爬取网址时，会开始爬取当前网址，并将爬取到的数据存储在`应用名称:item`中



##### 配置文件中的修改：

开启pipeline.py，使用redis提供的管道文件，而不是使用项目中默认的pipeline文件：

```python
# 开启pipeline.py，使用redis提供的管道文件，而不是使用项目中默认的pipeline文件
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 300,
}

# 调度器，引擎将爬虫文件中的请求对象，都发送给此调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# 表示使用scrapy_redis中的去重组件，去重调度器中的重复请求
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# 表示是否允许暂停，如果宕机或暂停后，爬取的过程可以从断开时开始
SCHEDULER_PERSIST = True

# 如果redis服务器不在本机，在其他机器，则需配置
REDIS_HOST = '192.168.3.82'
REDIS_PORT = 6379
```



##### 运行分布式爬虫程序的方法：

`scrapy runspider qiubai.py`



##### 执行过程：

执行程序后，程序会监听redis服务器，直到redis_key的队列中存放进了起始url

```shell
DEBUG: Telnet console listening on 127.0.0.1:6023
```



在redis数据库中当通过代码中的redis_key插入爬虫网址时，程序开始爬取数据：

```
lpush qiubai_key https://www.qiushibaike.com/pic/
```



##### 查询数据

```shell
# 先查询出有哪些key值
keys *
1) "qiubai:requests"
2) "qiubai:items"
3) "qiubai:dupefilter"

#在查询指定qiubai:items中的数据
lrange qiubai:items 0 -1
  1) "{\"img_url\": \"https://pic.qiushibaike.com/system/pictures/12143/121433224/medium/TG7FY0Y1Z9ESY3RE.jpg\"}"
  2) "{\"img_url\": \"https://pic.qiushibaike.com/system/pictures/12143/121433141/medium/6CS7CLT38DQNJ17O.jpg\"}"
```