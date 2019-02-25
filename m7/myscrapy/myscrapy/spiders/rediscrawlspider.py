# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import items

class RediscrawlspiderSpider(RedisCrawlSpider):
    name = 'rediscrawlspider'

    redis_key = 'mykey'

    link = LinkExtractor(allow=r'/pic/page/\d+')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        qiushi_list = response.xpath('//div[@id = "content-left"]/div')

        for qiushi in qiushi_list:
            img_url = 'https:' + qiushi.xpath('.//div[@class = "thumb"]/a/img/@src').extract_first()

            item = items.MyscrapyItem()
            item['img_url'] = img_url

            yield item
