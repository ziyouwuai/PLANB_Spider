#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy import cmdline

from zufangluntan.spiders.zufang import ZufangSpider
from zufangluntan.spiders.lianjia import LianJiaZuFangSpider

cmdline.execute(['scrapy', 'crawl', ZufangSpider.name])
# cmdline.execute(['scrapy', 'crawl', LianJiaZuFangSpider.name])
