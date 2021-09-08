import pymysql

from config import HOST, PORT, USER, PASSWORD, DATABASE


class ZuFangLunTanPipeline:

    def __init__(self):
        self.conn = pymysql.Connect(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DATABASE)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into zufangluntan(zufang_type, zufang_title, author_name, publish_time, reply, review, fabiao_name, fabiao_time, fang_desc) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, (
        item.get('zufang_type'),
        item.get('zufang_title'),
        item.get('author_name'),
        item.get('publish_time'),
        item.get('reply'),
        item.get('review'),
        item.get('fabiao_name'),
        item.get('fabiao_time'),
        item.get('fang_desc')))

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
