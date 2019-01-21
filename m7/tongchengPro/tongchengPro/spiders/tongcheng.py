# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class TongchengSpider(RedisCrawlSpider):
    name = 'tongcheng'

    redis_key = 'tongcheng'

    link = LinkExtractor(allow=r'pn\d+/')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.text)
