# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# use json to save data
import json
import codecs
import sys


class mingshiPipeline(object):
    def __init__(self):
        # you can change Han.json
        self.file = codecs.open('Han.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # change to determain json you like
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"

        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

