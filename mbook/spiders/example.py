# -*- coding: utf-8 -*-
import scrapy


class QianQianSpider(scrapy.Spider):
    name = 'qianqianxiaoshuo'
    allowed_domains = ['www.qianqianxs.com']
    start_urls = ['https://www.qianqianxs.com/']

    def parse(self, response):
        pass
