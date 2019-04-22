# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MafengwoPipeline(object):
    def process_item(self, item, spider):
        file_name = '/home/liumeng/paxiaochong/city.txt'
        with open(file_name,encoding='utf8',mode='a+') as file:
            file.write(item['city']+'\n')
        return item
