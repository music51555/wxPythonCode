`scrapy`框架之基于管道的数据持久化存储

`items`文件：存储解析到的页面数据

`pipelines`文件：处理持久化存储的相关操作



存储流程：

1、将解析到的数据存储到`item`对象

在items文件中声明属性

author = scrapy.Field()

在爬虫文件中创建item对象，赋值给items文件中的属性

2、使用`yield`关键字将`item`提交给管道文件进行处理

yield item

3、在管道文件中编写代码完成存储操作

yield的数据在Pipeline中接收item对象，并将对象中的数据进行持久化存储

在pipeline中通过item对象，获取属性值

在settings.py中开启pipeline，字典中的内容表示优先级

4、在配置文件中开启管道操作