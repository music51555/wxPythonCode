# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiTextPipeline(object):
    def process_item(self, item, spider):
        author = item['author']
        duanzi = item['duanzi']

        with open('qiubai.txt', 'w' , encoding='utf-8') as f:
            f.write(author+':'+duanzi+'\n\n\n')
