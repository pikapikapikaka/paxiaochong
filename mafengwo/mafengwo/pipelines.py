# -*- coding: utf-8 -*-
import os
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MafengwoPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='ddr4', db='mafengwo', port=3306, charset='utf8')
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):
        #db = pymysql.connect('localhost', 'root', 'ddr4', 'mafengwo')
        #point = db.cursor()#获取操作对象
        #组成sql语句
        id = item['id'].replace('\'','')
        sight = item['sight'].replace('\'','')
        telephone = item['telephone'].replace('\'','')
        play_time = item['play_time'].replace('\'','')
        ticket = item['ticket'].replace('\'','')
        open_time = item['open_time'].replace('\'','')
        traffic = item['traffic'].replace('\'','')
        where = item['where'].replace('\'','')
        sql = "insert into sight(id,sight,telephone,play_time,ticket,open_time, traffic, place) "\
              "values({},'{}','{}','{}','{}','{}','{}','{}')".format(int(id),sight, telephone,
                                                       play_time, ticket, open_time,
                                                       traffic, where)
        #point.excute(sql)
            # 执行sql语句
        self.cursor.execute(sql)
            # 提交到数据库执行
        self.connect.commit()
        print(item['where'],'handle on it!')


        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
