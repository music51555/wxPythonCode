# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    # allowed_domains = ['www.chouti.com']
    start_urls = ['https://dig.chouti.com/']

    link = LinkExtractor(allow=r'/all/hot/recent/\d+')

    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//a[@class = "show-content color-chag"]/text()').extract_first().strip()
        print(title)