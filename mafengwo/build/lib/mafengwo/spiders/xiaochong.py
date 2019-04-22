# -*- coding: utf-8 -*-
import scrapy
from mafengwo.items import  MafengwoItem
import os


class XiaochongSpider(scrapy.Spider):
    name = 'xiaochong'
    allowed_domains = ['www.mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/']
    #第一个执行的函数

    '''def start_requests(self):
        yield scrapy.Request("http://www.mafengwo.cn/mdd/",
                      headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                               'Referer':'https://www.mafengwo.cn/mdd/',
                               })'''



    def parse(self, response):
        #with open(file='/home/liumeng/paxiaochong/abc',mode='w+',encoding='utf8') as file:
        #   file.write("hello world")
        #上面代码也生效了
        every = []

        dalu = response.xpath("//div[@class='hot-list clearfix']/div/dl/dd/a/@href").extract()#获取国内的地址
        #other = response.xpath("//div[@class='hot-list clearfix hide']/div/dl/dd/a/@href").extract()#获取国外的地址
        every.extend(dalu)
        #every.extend(other)#将他们归并
        with open(file='/home/liumeng/paxiaochong/city',mode='w+',encoding='utf8') as file:
            file.write(' '.join(every))
        for i in range(len(every)):
            address = every[i]
            new_address = 'https://www.mafengwo.cn/jd/{}/gonglve.html'.format(address.split('/')[3].split('.')[0])#组装成新的地址
            #yield scrapy.Request(new_address, callback=self.parse_sight(response))#进行下载

    ''' city_list = response.xpath('//div[@class="col"]/dl/dt/a/text()').extract()
            for c in city_list:
                item = MafengwoItem()
                item['city'] = c
                yield  item#进行迭代
            '''

    # yield city_list
    # response.xpath("//div[@class='hot-list clearfix']/div/dl/dd/a/text()").extract()
    # 上面是爬去国内省市
    # response.xpath("//div[@class='hot-list clearfix hide']/div/dl/dd/a/text()").extract()
    # 以上为爬去其他地方
    # res1.split('/')[3].split('.')获取页面


    def parse_sight(self, response):
        city = response.xpath('//a[@class="drop"]/span[@class="hd"]/text()').extract()
        with open(file='/home/liumeng/paxiaochong/city.txt',mode='a+',encoding='utf8') as file:
            file.write(''.join(city))