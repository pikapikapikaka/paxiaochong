# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MafengwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()#地点名称
    sight = scrapy.Field()#景点名称
    summary = scrapy.Field()#简介
    play_time = scrapy.Field()#用时参考
    ticke = scrapy.Field()#门票
    open_time = scrapy.Field()#开放时间
    traffic = scrapy.Field()#交通
    where = scrapy.Field()#景点位置
    comment = scrapy.Field()#评论
    province = scrapy.Field()#省份


