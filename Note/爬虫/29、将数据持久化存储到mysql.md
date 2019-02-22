将数据持久化存储到`mysql`

**知识点1：**在`soup.select()`方法中如果要使用`nth-child(2)`，要写为`nth-of-type(2)`

**知识点2：**一定要记住如果想做持久化存储，那么一定要使用`yield item`关键，和在`settings.py`中开启`pipeline`设置

```python
# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import QiubaiForMysqlItem


class QiubaiMysqlSpider(scrapy.Spider):
    name = 'qiubai_mysql'

    start_urls = ['http://www.qiushibaike.com/text']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        div_list = soup.select('#content-left > div')

        for div in div_list:
            author = div.select('.author h2')[0].text
            content = div.select('.content > span')[0].text

            item = QiubaiForMysqlItem()
            item['author'] = author
            item['content'] = content

            yield item
```



**知识点1：**在`pymysql`配置信息中，不要写为`utf-8`，而是写为`utf8`

**知识点2：`try...exception conn.rollback`**，捕获到异常时调用`conn`的`rollback`方法回滚

**知识点3：`insert into xx values`**不要写为`value`

```python
import pymysql

class QiubaiForMysqlPipeline(object):

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='140.143.132.118',
            port=3306,
            user='xiaoxin',
            password='Nishi458_2',
            db='qiubai',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()
        self.sql = 'insert into qiushi(author,content) values(%s,%s)'

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        try:
            self.cursor.execute(self.sql,(author,content))
            self.conn.commit()
        except Exception:
            self.conn.rollback()


    def close_spiter(self,spiter):
        self.cursor.close()
        self.conn.close()
```

