#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request
from loguru import logger


class LianJiaZuFangSpider(scrapy.Spider):
    name = 'lianjiazufang'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang/pg1/#contentList']

    def parse(self, response):
        div_list = response.css('div.content__list--item')
        for div in div_list:
            title = div.css('a.twoline::text').extract_first().strip()
            desc_list = div.css('p.content__list--item--des *::text').extract()
            desc_list[-2] = desc_list[-2].replace(' ', '')
            desc = ''.join([desc.strip() for desc in desc_list])
            price = ''.join(div.css('span.content__list--item-price *::text').extract())
            logger.info(f'租房标题 --> {title} 价格 --> {price} 租房描述 --> {desc}')
        page_div = response.xpath('//div[@class="content__pg"]').extract_first()
        total_page, cur_page = re.findall(r'data-totalpage="(\d+)" data-curpage="(\d+)"', page_div)[0]
        if int(total_page) > int(cur_page):
            next_url = f'https://bj.lianjia.com/zufang/pg{int(cur_page) + 1}/#contentList'
            yield Request(url=next_url, callback=self.parse)