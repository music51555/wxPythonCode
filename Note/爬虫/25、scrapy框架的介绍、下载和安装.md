`scrapy`框架

**scrapy**：美  `skræpi`爬虫

**介绍：**

为了爬取网站数据而编写的应用框架

提供高性能的异步下载，解析，持久化存储等功能



**安装：**

##### **`linux mac`：**

`pip3 install scrapy`



##### **`windows`:**

**1、**`pip3 install wheel`，和`egg`一样，是一种打包格式

**2、**下载`Twisted`,`Twisted`是用`python`实现的基于事件驱动的网络引擎框架 

首先通过`python3 -V`命令查询出`python`版本后选择对应的内容下载

`https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted`

`pip3 install 下载的框架.whl`

**3、**`pip3 install pywin32`，`python`可以直接操控`win32`程序 

**4、**`pip3 install scrapy`，为了爬取网站数据而编写的应用框架

**5、**终端输入`scrapy`测试



**执行流程：**

##### 1、创建一个`scrapy`项目

`scrapy startproject myscrapy`

```python
- projectname
	- projectname
		- spiders # 在该目录下编写爬虫文件
			- __init__.py
		- __init__.py
		- items.py # 数据结构化：将在爬虫文件中解析的数据进行数据结构化
		- middlewares.py # 中间件
		- pipelines.py # 管道文件：持久化存储处理
		- settings.py # 配置文件：递归层数、并发数、延迟下载等
	- scrapy.cfg # 项目主配置文件：一般不进行修改
```





##### 2、创建爬虫文件

**spider**  `/'spaɪdɚ/ ` 蜘蛛；设圈套者 

**2.1、**首先进入项目目录

```
cd myscrapy
```

**2.2、**创建爬虫文件，创建成功后会在`spiders`目录下创建成功一个爬虫文件

```
scrapy genspider 爬虫文件名称scrapy_for_qiubai 指定域名www.qiushibaike.com
```





##### 3、在文件中编写爬虫程序

**爬虫方法`parse`必须返回一个可迭代对象，或空**

```python
# -*- coding: utf-8 -*-
import scrapy

# 所有的爬虫类都继承于scrapy.Spider父类
class ScrapyForQiubaiSpider(scrapy.Spider):
    
    # 爬虫文件的名称，当在spider文件夹下有多个爬虫文件时，通过name变量定位到一个具体的爬虫文件
    name = 'scrapy_for_qiubai'
    
    # 允许爬取的域名网站，列表集合，一般注释掉，如果没有注释，那么无法爬取到该域名以外的图片
    allowed_domains = ['www.qiushibaike.com']
    
    # 起始url
    start_urls = ['http://www.qiushibaike.com/']

    # 对获取的页面内容进行解析
    # response根据起始url发起请求后请求成功的响应对象
    def parse(self, response):
        
        # 通过text方法获取页面的内容
        print(response.text)
```





##### 4、编写配置文件

**4.1、**是否遵从网站的`ROBOTS`协议，如`https://www.baidu.com/robots.txt`，默认为`True`，改为`False`

```
ROBOTSTXT_OBEY = True
```

**4.2、**修改`USER_AGENT`

```
USER_AGENT = 'user-agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
```





##### 5、执行

**crawl**  `美 /krɔl/ `  爬行 

```python
scrapy crawl 爬虫应用文件

# 添加--nolog参数，会不显示日志信息
scrapy crawl scrapy_for_qiubai --nolog
```

