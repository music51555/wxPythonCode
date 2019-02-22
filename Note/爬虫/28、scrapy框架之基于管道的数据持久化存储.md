`scrapy`框架之基于管道的数据持久化存储

`items.py`：存储解析到的页面数据

`pipelines.py`：将数据持久化存储保存到文件



存储流程：

##### 1、将解析到的数据存储到`item`对象

创建项目后，在项目目录下会生成`items.py`文件

引入`items`文件后，创建文件内以项目名称创建的类的对象

```python
from .. import items

item = items.QiubaiTextItem()
item['author'] = author
item['duanzi'] = duanzi
```



`items`文件用于存储页面解析到的数据，内容为：

```python
import scrapy

class MyscrapyItem(scrapy.Item):
    author = scrapy.Field()
    content = scrapy.Field()
```



##### 2、使用`yield`关键字将`item`提交给管道文件进行处理

```python
from .. import items

item = items.QiubaiTextItem()
item['author'] = author
item['duanzi'] = duanzi

# 通过yield返回item对象，对象包含准备持久化处理的属性，将对象返回到pipeline.py文件中,会被执行process_item函数
yield item
```



##### 3、在管道文件中编写代码完成存储操作

接收到`item`对象后，获取对象内的属性，将属性写入到文件中

```python
class QiubaiTextPipeline(object):
    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        with open('qiubai.txt', 'w' , encoding='utf-8') as f:
            f.write(author+':'+duanzi+'\n\n\n')
```



##### 4、在配置文件中开启管道操作

在`settings.py`中开启`pipeline`，字典中的内容表示优先级

```python
ITEM_PIPELINES = {
   'qiubai_text.pipelines.QiubaiTextPipeline': 300,
}
```



##### 附加方法：`open_spider(self,spider)`和`close_spider(self,spider)`

如果在`pipeline.py`中执行数据存储，如果使用`w`模式的话，那么每次`yield`到`process_item`函数时，都会重新将新数据写入该文件，导致文件的内容都是最后一次存储的数据，我们可以使用`a`模式，在文件内容结尾添加

不过`scrapy`为我们提供了两个方法，分别是`open_spider(self,spider)`和`close_spider(self,spider)`，分别在爬虫应用开始前和结束后各只执行一次

```python
class QiubaiTextPipeline(object):
    def open_spider(self,spider):
        self.f = open('qiubai.txt', 'a' , encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        self.f.write(author+':'+duanzi+'\n\n\n')

    def close_spider(self,spider):
        self.f.close()
```

