# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import redis

class QiubaiForMysqlPipeline(object):

    def open_spider(self,spider):
        self.conn = redis.Redis(host='127.0.0.1', port=6379, charset='utf8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        dict = {
            'author': author,
            'content': content
        }

        self.conn.lpush('qiubai_data', str(dict))


