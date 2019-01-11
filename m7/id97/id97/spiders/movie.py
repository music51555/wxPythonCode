# -*- coding: utf-8 -*-
import scrapy
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import items


class MovieSpider(scrapy.Spider):
    name = 'movie'

    start_urls = ['http://www.55xia.com/movie']

    def movie_detail(self, response):
        detail_labels = response.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[2]/table/tbody/tr')
        author = detail_labels[0].xpath('//td[2]/a/text()').extract_first()
        release_time = detail_labels[6].xpath('td[2]/text()').extract_first()

        item = response.meta['item']
        item['author'] = author
        item['release_time'] = release_time

        yield item

    def parse(self, response):
        movie_list = response.xpath('//div[@class = "col-xs-1-5 col-sm-4 col-xs-6 movie-item"]')
        for movie in movie_list:
            movie_name = movie.xpath('.//div[@class = "meta"]/h1/a/text()').extract_first()
            movie_score = movie.xpath('.//div[@class = "meta"]/h1/em/text()').extract_first()
            movie_type = ','.join(movie.xpath('.//div[@class = "otherinfo"]//text()').extract()[1:])

            movie_detail_url = 'http://' + movie.xpath('//a[@title = "'+ movie_name +'"]/@href').extract_first()

            item = items.Id97Item()
            item['movie_name'] = movie_name
            item['movie_score'] = movie_score
            item['movie_type'] = movie_type

            yield scrapy.Request(url = movie_detail_url, callback=self.movie_detail, meta = {'item': item})

