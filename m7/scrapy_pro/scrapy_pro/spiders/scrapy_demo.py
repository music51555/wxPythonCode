# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from bs4 import BeautifulSoup
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import ScrapyProItem


class ScrapyDemoSpider(scrapy.Spider):
    name = 'scrapy_demo'

    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        div_list = soup.select('#content-left > div')

        for div in div_list:
            author = div.select('.author h2')[0].text
            content = div.select('.content > span')[0].text

            item = ScrapyProItem()
            item['author'] = author
            item['content'] = content

            yield item


