# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()#旅游景点唯一id

    sight = scrapy.Field()#景点名称
    telephone = scrapy.Field()#电话
    play_time = scrapy.Field()#用时参考
    ticket = scrapy.Field()#门票
    open_time = scrapy.Field()#开放时间
    traffic = scrapy.Field()#交通
    where = scrapy.Field()#景点位置#在数据库，需要改成place
    good_comment = scrapy.Field()#好评
    middle_comment = scrapy.Field()#中评
    low_comment = scrapy.Field()#差评
    #other_comment = scrapy.Field()#其他评论


