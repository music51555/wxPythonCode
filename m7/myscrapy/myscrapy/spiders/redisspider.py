# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import items

class RedisspiderSpider(scrapy.Spider):
    name = 'redisspider'

    redis_key = 'mykey'

    def parse(self, response):
        qiushi_list = response.xpath('//div[@id = "content-left"]/div')

        for qiushi in qiushi_list:
            img_url = 'https:' + qiushi.xpath('.//div[@class = "thumb"]/a/img/@src').extract_first()

            item = items.MyscrapyItem()
            item['img_url'] = img_url

            yield item
