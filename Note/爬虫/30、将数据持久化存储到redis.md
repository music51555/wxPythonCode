将数据持久化到`redis`

**知识点1：**`redis`创建连接对象`self.conn = redis.Redis(host='127.0.0.1', port=6379, charset='utf8')`

**知识点2：**直接将字典存如`redis`，提示`redis.exceptions.DataError: Invalid input of type: 'dict'. Convert to a byte, string or number first`错误，转换为`str`类型后正确存入

**知识点3：`redis`**存储数据调用`conn.lpush(key,value)`方法

```python
import pymysql
import redis

class QiubaiForMysqlPipeline(object):

    def open_spider(self,spider):
        self.conn = redis.Redis(host='127.0.0.1', port=6379, charset='utf8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        dict = {
            'author': author,
            'content': content
        }

        self.conn.lpush('qiubai_data', str(dict))
```

