import scrapy

from zufangluntan.items import ZufangluntanItem


class ZufangSpider(scrapy.Spider):
    name = 'zufangluntan'
    allowed_domains = ['www.weizan.cn']
    start_urls = ['https://www.weizan.cn/f/s-1030440?page=1&typeId=0']

    def parse(self, response):
        result_list = response.css('.all_theme_content_li')
        for resp in result_list:
            if resp.css('div.all_theme_icon_top_kuang img.all_theme_icon_file'):
                zufang_type = resp.css('a.color_blue02::text').extract_first()
                zufang_title = resp.css('a.text::text').extract_first()
                author_name = resp.css('div.author_name a::text').extract_first()
                publish_time = resp.css('div.author_name span::text').extract_first()
                reply = int(resp.css('div.huifu a::text').extract_first(0))
                review = int(resp.css('div.huifu span::text').extract_first(0))
                fabiao = resp.css('div.fabiao a::text').extract()
                fabiao_name, fabiao_time = None, None
                if fabiao:
                    fabiao_name, fabiao_time = fabiao
                cb_dict = {'zufang_type': zufang_type, 'zufang_title': zufang_title, 'author_name': author_name,
                           'publish_time': publish_time, 'reply': reply, 'review': review, 'fabiao_name': fabiao_name,
                           'fabiao_time': fabiao_time}
                zufang_detail = resp.css('a.text::attr(href)').extract_first()
                yield response.follow(zufang_detail, callback=self.parse_detail, cb_kwargs=cb_dict)
        if response.css('.division_bottom'):
            next_page_url = response.css('.division_bottom a::attr(href)').extract_first()
            yield response.follow(next_page_url, callback=self.parse)

    def parse_detail(self, response, **kwargs):
        item = ZufangluntanItem(**kwargs)
        detail_content = response.css('div.post_content *::text').extract()
        desc = ''
        for detail in detail_content:
            desc += detail.strip()
        item['fang_desc'] = desc
        yield item
