# -*- coding: utf-8 -*-
import scrapy
from .. import items


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    # allowed_domains = ['www.douban.com']
    start_urls = ['http://www.qiushibaike.com/text']

    def parse(self, response):
        qiushi_list = response.xpath('//div[@id = "content-left"]/div')
        item = items.MyscrapyItem()

        for qiushi_item in qiushi_list:
            author = qiushi_item.xpath('.//div[@class="author clearfix"]//h2/text()').extract_first()
            qiushi = qiushi_item.xpath('.//div[@class="content"]/span/text()').extract()

            content = ''
            for content_item in qiushi:
                content+=content_item

                item['author'] = author
                item['content'] = content

                yield item

