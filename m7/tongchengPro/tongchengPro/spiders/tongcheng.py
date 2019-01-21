# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import os,sys
import time


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

            print(house_info)
