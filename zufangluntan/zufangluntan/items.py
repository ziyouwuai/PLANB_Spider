
import scrapy


class ZufangluntanItem(scrapy.Item):
    zufang_type = scrapy.Field()
    zufang_title = scrapy.Field()
    author_name = scrapy.Field()
    publish_time = scrapy.Field()
    reply = scrapy.Field()
    review = scrapy.Field()
    fabiao_name = scrapy.Field()
    fabiao_time = scrapy.Field()
    fang_desc = scrapy.Field()
