# -*- coding: utf-8 -*-
import scrapy

from mbook.utils.chinese2num import chinese2num
from mbook.utils.parseChapterStr import parseChapterStr


class QianQianSpider(scrapy.Spider):
    name = 'qianqianxiaoshuo'
    allowed_domains = ['www.qianqianxs.com']
    start_urls = ['https://www.qianqianxs.com/113/113162/']

    def parse(self, response):
        try:
            for li in response.selector.css('.panel-body .list-group li:not(.list-group-item)'):
                name = li.xpath('a/text()')[0].extract()
                chapterData = parseChapterStr(name)
                chapterData['link'] = 'https://www.qianqianxs.com' + li.xpath('a/@href')[0].extract()
                chapterData['select'] = '.content-body'
                print(chapterData)
            pass
        except Exception:
            print(Exception)
            pass
