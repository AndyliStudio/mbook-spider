# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MongoDBPipeline(object):

    def __init__(self):
        url = ''
        if settings['MONGO_AUTH']:
            url = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authMechanism=MONGODB-CR".format(
                username=settings['MONGODB_USER'], password=settings['MONGODB_PASS'], host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], db_name=settings['MONGODB_DB'])
        else:
            url = "mongodb://{host}:{port}/{db_name}?authMechanism=MONGODB-CR".format(
                host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'], db_name=settings['MONGODB_DB'])

        connection = pymongo.MongoClient(url)
        db = connection[settings['MONGODB_DB']]
        self.Book = db['mbooks']
        self.Chapter = db['chapters']
    
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.Chapter.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item


class MbookPipeline(object):
    def process_item(self, item, spider):
        return item
