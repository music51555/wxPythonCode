# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    start_urls = ['http://dig.chouti.com/']

    # 实例化链接提取器对象，通过传入的正则表达式在页面中匹配数据，提取器将得到的
    link = LinkExtractor(allow=r'/all/hot/recent/\d+')

    # 实例化规则解析器对象,将链接提取器传入规则解析器，并调用parse_item回调函数，follow表示是否在新的页面中继续应用链接提取器的中的正则表达式提取链接数据
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        response.xpath('//div[@class = "item"]')
