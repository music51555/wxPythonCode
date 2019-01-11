通过`scrapy`框架抓取糗事百科数据

**知识点1：**注释`allowed_domains`列表，表示抓取不仅仅是域名下的图片

**知识点2：**`response`响应对象提供了`xpath`方法，可以通过`xpath`获取响应内容中的标签对象，调用`xpath`方法

**知识点3：**通过`response.xpath`得到的结果是一个列表

**知识点4：**在`response.xpath`结果中可以调用`extract()[0]`方法和`extract_first()`得到列表中的结果

**知识点5：**在得到的`xpath`结果中的元素，仍然支持`xpath`方法，继续查找时应添加`.//`或`./`查找

**知识点6：**如果要得到标签对象的属性，如`href`，`xpath`方法提供了`//div/a/@href`方法

```python
# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        content_list = response.xpath('//div[@id="content-left"]/div')

        for content_item in content_list:
            # 通过scrapy封装的response.xpath得到的结果是一个列表，存储的是selector类型的结果，如[<Selector xpath='./div/div/a[2]/h2/text()' data='\n木子：李\n'>,
            # 所以通过提供extract()或extract_first()方法得到列表中的每一个值
            author = content_item.xpath('./div/a[2]/h2/text()').extract_first()
            content = content_item.xpath('.//div[@class = "content"]/span[1]/text()').extract()
			
            # 在结果列表中如果单纯的通过extract_first()方法取出数据，有的段子内容是换行的，只得到了第一句结果，所以循环列表的内容，连接起来展示
            duanzi = ''
            for item in content:
                duanzi+=item

            print(author)
            print(duanzi)
```





