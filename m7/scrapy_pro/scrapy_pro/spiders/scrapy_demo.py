# -*- coding: utf-8 -*-
import scrapy

class ScrapyDemoSpider(scrapy.Spider):
    name = 'scrapy_demo'

    start_urls = ['https://www.baidu.com/s?ie=utf-8&wd=ip']

    def parse(self, response):
        with open('ip.html', 'w', encoding='utf-8') as f:
            f.write(response.text)


