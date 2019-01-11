# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Id97Pipeline(object):
    def process_item(self, item, spider):
        content ='电影名称：'+item['movie_name']+'\n'+\
        '电影评分：'+item['movie_score']+'\n'+\
        '电影类型：'+item['movie_type']+'\n'+\
        '导演:'+item['author']+'\n'+\
        '上映时间:'+str(item['release_time'])+'\n\n\n\n'

        with open('id97_movie_info.txt', 'a', encoding='utf-8') as f:
            f.write(content)

        return item
