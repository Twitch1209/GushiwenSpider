# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrpay.selector import Selector
from w3lib.html import remove_tags
from _mysql_exceptions import IntegrityError
import MySQLdb
import redis
import re


class GushiwenspiderPipeline(object):
    def process_item(self, item, spider):
        return item
