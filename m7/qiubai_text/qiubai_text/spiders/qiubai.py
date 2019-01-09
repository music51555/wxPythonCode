# -*- coding: utf-8 -*-
import scrapy

from .. import items

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        content_list = response.xpath('//div[@id="content-left"]/div')

        data_list = []
        for content_item in content_list:
            # 通过scrapy封装的response.xpath得到的结果是一个列表，存储的是selector类型的结果，如[<Selector xpath='./div/div/a[2]/h2/text()' data='\n木子：李\n'>,
            # 所以通过提供extract()或extract_first()方法得到列表中的每一个值
            author = content_item.xpath('./div/a[2]/h2/text()').extract_first()
            content = content_item.xpath('.//div[@class = "content"]/span[1]/text()').extract()

            duanzi = ''
            for item in content:
                duanzi+=item

            item = items.QiubaiTextItem()
            item['author'] = author
            item['duanzi'] = duanzi

            yield item
