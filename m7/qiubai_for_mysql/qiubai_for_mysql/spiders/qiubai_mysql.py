# -*- coding: utf-8 -*-
import scrapy
import sys
import os
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from items import QiubaiForMysqlItem


class QiubaiMysqlSpider(scrapy.Spider):
    name = 'qiubai_mysql'

    start_urls = ['http://www.qiushibaike.com/text']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        div_list = soup.select('#content-left > div')

        for div in div_list:
            author = div.select('.author h2')[0].text
            duanzi = div.select('.content > span')[0].text

            item = QiubaiForMysqlItem()
            item['author'] = author
            item['duanzi'] = duanzi

            print('---------item----------',item)

            yield item
