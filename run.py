#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 入口文件

import sys
import getopt
import logging
import time
from mbook.utils.connecMongo import MongoDBConnect
from twisted.internet import reactor, defer
from scrapy.crawler import Crawler
from scrapy import signals
from mbook.spiders.update import MbookUpdateSpider
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
crawler = Crawler(settings)
crawler.configure()

def main():
    spiderName = ''
    mongo = MongoDBConnect()
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['name='])
    except getopt.GetoptError:
        print('python mbook/run.py --name [spider name]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('python mbook/run.py --name [spider name]')
            sys.exit()
        elif opt == '--name':
            spiderName = arg

    if spiderName == 'update':
        print('开始执行更新爬虫...')
        print('当前时间：' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 获取需要更新的数据
        needUpadteBooks = mongo.Book.find({'source': {'$exists': True}})
        updateBookCrawl(needUpadteBooks)
        crawler.start()


def updateBookCrawl(books):
  for book in books:
    crawler.crawl(MbookUpdateSpider, source=book.source)

if __name__ == "__main__":
    main()
