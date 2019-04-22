# -*- coding: utf-8 -*-
import scrapy
from mafengwo.items import  MafengwoItem
import re#加载正则
import json
import mafengwo.spiders.parse_html as html
from bs4 import BeautifulSoup
import mafengwo.spiders.forrequests as request
import selenium.webdriver
import time


class XiaochongSpider(scrapy.Spider):
    name = 'xiaochong'
    allowed_domains = ['www.mafengwo.cn']
    start_urls = ['http://www.mafengwo.cn/mdd/']
    #第一个执行的函数
    def parse(self, response):#解释首页地址
        every = []
        dalu = response.xpath("//div[@class='hot-list clearfix']/div/dl/dd/a/@href").extract()#获取国内的地址
        #other = response.xpath("//div[@class='hot-list clearfix hide']/div/dl/dd/a/@href").extract()#获取国外的地址
        every.extend(dalu)#将国内地址，放到列表里
        #every.extend(other)#将他们归并
        print(every)
        for i in range(len(every)):
            address = every[i]
            number = address.split('/')[3].split('.')[0]
            new_address = 'https://www.mafengwo.cn/jd/{}/gonglve.html'.format(number)#组装成新的地址
            yield scrapy.Request(new_address, callback=self.parse_sight, meta={'city_number':number,'url':new_address})#进行下载

    def parse_sight(self, response):#解释城市
        city = response.css('.hd').css('a::text').extract()#查看当前获取的城市名称

        print('正在爬取',city)
        number = response.meta['city_number']#获取到编号
        url = response.meta['url']#用selenium获取当前页面，以找到景点数据
        option = selenium.webdriver.FirefoxOptions()
        option.set_headless()
        browser = selenium.webdriver.Firefox(options=option)
        browser.get(url=url)
        sight_href = browser.find_elements_by_xpath('//div[@class="bd"]/ul/li')
        for i in sight_href:
            a = i.find_element_by_tag_name('a')
            url = a.get_attribute('href')
            print('selenium获取到的链接', url)
            yield scrapy.Request(url=url, callback=self.parse_sight_content, meta={'link_number':number})
        #查看下一页选项
        try:
            next_page = browser.find_element_by_link_text('后一页')
        except:
            next_page = None
        while next_page:
            time.sleep(3)
            next_page.click()
            # print(browser.find_elements_by)
            sight_href = browser.find_elements_by_xpath('//div[@class="bd"]/ul/li')
            for i in sight_href:
                #print(i.text)
                a = i.find_element_by_tag_name('a')
                url = a.get_attribute('href')
                print('selenium地址：', url)
                zz_result = re.search('(\d*)\.html', url)
                num = zz_result.group(1)
                print('景点num:',num)
                yield scrapy.Request(url=url, callback=self.parse_sight_content, meta={'link_number':num})
                #print(url)
            try:
                next_page = browser.find_element_by_link_text('后一页')
            except:
                next_page = None
        print(city,'遍历结束！')


    def parse_sight_content(self, response):#解析景点的内容
        item = MafengwoItem()
        item['ticket'] = '无'
        try:
            item['play_time'] = response.css('.item-time').css('.content::text').extract()[0].replace('\'','')  # 用时
        except:
            item['play_time'] = "无"
        try:
            item['telephone'] = ''.join(response.css('.tel').css('.content::text').extract()).replace('\'','')#获取电话号码
        except:
            item['telephone'] = '无'
        try:
            item['ticket'] = response.css('[class="mod mod-detail"]').css('dl').css('div::text').extract()[0].replace('\'','')#价钱
        except:
            item['ticket'] = '无'
        try:
            res = response.css('[class="mod mod-detail"]').css('dd').extract()  # 获取一系列数据
            item['traffic'] = res[0].replace('\'','')#交通信息
            item['open_time'] = res[2].replace('\'','')#开放时间
        except:
            #item['ticket'] = '无'
            item['traffic'] = '无'  # 交通信息
            item['open_time'] = '无'  # 开放时间
        try:
            item['where'] = response.css('.hd').css('a::text').extract()[0].replace('\'','')#景点所在地
        except:
            item['where'] = '错误'
        item['sight'] = ''.join(response.css('[class="title"]').css('h1::text').extract()).replace('\'','')  # 景点名称
        #print(item)
        #获取评论的url
        link_number = response.meta['link_number']#获取poi的值，进行传递
        item['id'] = link_number.replace('\'','')
        print('当前以获取信息：',item)
        yield item
        #url='http://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?callback=jQuery181030927871783778926_1555549642490&params={"poi_id":'+str(link_number)+'}&_ts=1555549642655&_sn=d7d8e4cc9a&_=1555549642657'

        '''headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Host': 'pagelet.mafengwo.cn',
            'Referer': 'http://www.mafengwo.cn/poi/{}.html'.format(str(link_number))
        }'''
        #yield scrapy.Request(url=url, callback=self.parse_sight_content_post, headers=headers, meta={'data':item})

    def parse_sight_content_post(self, response):
        #print('现在是评论信息：')
        #print(response.meta['data'])
        #print(response.text)
        d = html.parse_sight_comment(sentence=response.text)
        item = response.meta['data']
        item['good_comment'] = d[0]
        item['middle_comment'] = d[1]
        item['low_comment'] = d[2]
        print('完整结果：', item)
        yield item
