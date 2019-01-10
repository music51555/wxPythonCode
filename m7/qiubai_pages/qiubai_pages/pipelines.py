# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiPagesPipeline(object):
    def open_spider(self,spider):
        self.f = open('qiubai.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.f.write(author+':'+'\n'+content+'\n\n')

    def close_spider(self,spider):
        self.f.close()
