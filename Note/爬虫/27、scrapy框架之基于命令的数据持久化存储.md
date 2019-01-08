`scrapy`框架之基于命令的数据持久化存储

**知识点1：**将数据封装在字典中，在添加至列表中进行返回，字典中的`key`为导出文件中的列名

**知识点2：**执行`scrapy crawl qiubai -o qiubai.csv --nolog`将结果导出为文件

**知识点3：**如果导出内容为乱码，则在`settings.py`中设置`FEED_EXPORT_ENCODING = 'gbk'`



##### 1、保证`parse`方法返回的是一个可迭代对象，或者空

```python
# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        content_list = response.xpath('//div[@id="content-left"]/div')

        data_list = []
        for content_item in content_list:
            author = content_item.xpath('./div/a[2]/h2/text()').extract_first()
            content = content_item.xpath('.//div[@class = "content"]/span[1]/text()').extract()

            duanzi = ''
            for item in content:
                duanzi+=item
			
            # 每一次循环将结果封装在一个字典中，再将字典添加到列表中，返回一个可迭代的对象
            duanzi_info = {
                'author': author,
                'content': content
            }

            data_list.append(duanzi_info)

        return data_list
```



##### 2、通过命令进行持久化存储

内容被导出为`csv`格式，按照字典中的`key`值展示列值

```
scrapy crawl qiubai -o qiubai.csv --nolog
```



如果中文显示为乱码，则需要进行配置

```
FEED_EXPORT_ENCODING = 'gbk'
```

