`pipeiline`文件之执行多个类的持久化存储操作

**知识点1：**如果有多个类需要执行，需要在每一个类的`process_item`函数中返回`return item`，否则下一个类执行时`item`类型显示为`NoneType`

**知识点2：**在`author = item['author']`时，不要写为`author = item('author')`括号的形式

**知识点3：**如果需要执行多个`pipeline`类时，要在`settings.py`中开启多个类，并设置优先级，依次执行

```python
ITEM_PIPELINES = {
   'qiubai_for_mysql.pipelines.TxtPipeline': 300,
   'qiubai_for_mysql.pipelines.MysqlTestPipeline': 400,
   'qiubai_for_mysql.pipelines.RedisPipeline': 500,
}
```



```python
import pymysql
import redis

class TxtPipeline(object):
    def open_spider(self,spider):
        self.f = open('qiubai.txt', 'a' , encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        self.f.write(author+':'+duanzi+'\n\n\n')

        return item

    def close_spider(self,spider):
        self.f.close()

class MysqlTestPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='140.143.132.118',
            port=3306,
            user='xiaoxin',
            password='Nishi458_2',
            db='qiubai',
            charset='utf8'
        )
        self.sql = 'insert into qiushi(author, content) values(%s,%s)'
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        author = item['author']
        duanzi = item['duanzi']

        try:
            self.cursor.execute(self.sql,(author,duanzi))
            self.conn.commit()
        except Exception:
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

class RedisPipeline(object):

    def open_spider(self, spider):
        self.conn = redis.Redis(
            host='127.0.0.1',
            port=6379,
            charset='utf8'
        )

    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        qiushi = {
            'author': author,
            'duanzi': duanzi
        }

        self.conn.lpush('qiubai', str(qiushi))

        return item

```

