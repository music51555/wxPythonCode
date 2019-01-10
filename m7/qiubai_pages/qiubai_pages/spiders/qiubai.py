# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from .. import items


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'

    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        qiushi_list = soup.select('#content-left > div')
        next = soup.select('.next')

        for qiushi in qiushi_list:
            author = qiushi.select('.author h2')[0].text
            content = qiushi.select('.content > span')[0].text

            item = items.QiubaiPagesItem()
            item['author'] = author
            item['content'] = content

            yield item

        if next:
            next_url = 'https://www.qiushibaike.com' + soup.select('.pagination li a')[-1]['href']
            yield scrapy.Request(url = next_url, callback=self.parse)





