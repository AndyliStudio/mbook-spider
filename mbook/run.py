#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 入口文件

import sys
import getopt
import logging
from mbook.utils.connecMongo import MongoDBConnect

def main():
    spiderName = ''
    mongo = MongoDBConnect()
    try:
        opts = getopt.getopt(sys.argv[1:], 'h', ['name='])
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
      # 获取需要更新的数据
      needUpadteBooks = mongo.Book.find()
      print(needUpadteBooks)

if __name__ == "__main__":
    main()
