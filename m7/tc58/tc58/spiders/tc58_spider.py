# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class Tc58SpiderSpider(RedisCrawlSpider):
    name = 'tc58_spider'

    redis_key = '58tc'

    link = LinkExtractor(allow=r'/ershoufang/pn\d+/')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.text)
        house_info_list = response.xpath('//ul[@class = "house-list-wrap"]/li')

        for house_info in house_info_list:
            lease_title = house_info.xpath('.//h2[@class = "title"]/a/text()').extract_first().strip()

            print(lease_title)

