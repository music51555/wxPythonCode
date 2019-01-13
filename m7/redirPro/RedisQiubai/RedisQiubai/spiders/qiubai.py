# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import RedisqiubaiItem

class QiubaiSpider(RedisCrawlSpider):
    name = 'qiubai'

    redis_key = 'qiubai_key'

    link = LinkExtractor(allow=r'/pic/page/\d+')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        qiushi_list = response.xpath('//div[@id = "content-left"]/div')

        for qiushi in qiushi_list:
            img_url = 'https:' + qiushi.xpath('.//div[@class = "thumb"]/a/img/@src').extract_first()

            item = RedisqiubaiItem()
            item['img_url'] = img_url

            yield item
