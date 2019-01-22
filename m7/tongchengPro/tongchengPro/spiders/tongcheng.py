# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import os,sys
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from tongchengPro.items import TongchengproItem

class TongchengSpider(RedisCrawlSpider):
    name = 'tongcheng'

    redis_key = 'tongcheng'

    link = LinkExtractor(allow=r'ershoufang/pn\d+/')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('开始执行爬虫程序ing')

        house_list = response.xpath('//ul[@class = "house-list-wrap"]/li')

        for house in house_list:
            house_info = house.xpath('.//h2[@class = "title"]/a/text()').extract_first().strip()
            house_detail_url = house.xpath('.//h2[@class = "title"]/a/@href').extract_first()
            address = house.xpath('//p[@class = "baseinfo"]/span/a/text()').extract_first().strip()
            price = house.xpath('//p[@class = "sum"]/b/text()').extract_first()+'万'
            public_time = house.xpath('//div[@class = "time"]/text()').extract_first()

            item = TongchengproItem()
            item['house_info'] = house_info
            item['address'] = address
            item['price'] = price
            item['public_time'] = public_time

            yield scrapy.Request(url=house_detail_url, callback=self.house_detail, meta = {'item': item})

    def house_detail(self, response):
        detail = response.xpath('//p[@class = "pic-desc-word"]/text()').extract_first()
        item = response.meta['item']
        item['detail'] = detail

        print(item['house_info'])
        print(item['address'])
        print(item['price'])
        print(item['public_time'])
        print(item['detail'])

        # yield item
