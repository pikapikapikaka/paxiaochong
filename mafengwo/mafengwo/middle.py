'''import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.mafengwo.cn/ajax/router.php'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Referer': 'https://www.mafengwo.cn/jd/10128/gonglve.html',
    'Host': 'www.mafengwo.cn'
}
post_data = {'sAct': 'KMdd_StructWebAjax|GetPoisByTag', 'iMddid': str(10128), 'iTagId': '0', 'iPage': '1',
             '_ts': '1555680355764', '_sn': '4063b0c3ff'}
resp = requests.get('https://www.mafengwo.cn/jd/10128/gonglve.html', headers=header)
data = {'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
        'iMddid': '10128', 'iTagId': '0', 'iPage': '1', '_ts': '1555681894506',
        '_sn': 'c6918f6401'}
# print(resp.text)

response = requests.post(url=url, headers=header, data=data)
# print(response)
text = response.text
text = eval(text)
# print(type(text))#字典类型
content = text['data']['list']  # 获取内容列表
content = content.replace('\/', '/')  # 需要进行转义
soup = BeautifulSoup(content, 'html.parser')  #
a_result = soup.find_all('a')
res=[]
for i in a_result:
    #print('地：',i.get('href'))
    res.append(i.get('href'))
for i in res:
    pass
    #print(type(re.search('(\d*)\.', i).group(1)))

d = {0:'11',1:'22'}
print(d[0])
    # s = BeautifulSoup(i,'html.parser')
    # print(s.href)
#print(a_result)
# print(content)

content = text['data']['page']
soup = BeautifulSoup(content, 'html.parser')
res = soup.find(class_='count')
group = re.search('<span>\d*',str(res))
print(group.group(0).lstrip('<span>'))'''
import requests
import random
import selenium.webdriver
import pymysql
#browser = selenium.webdriver.Firefox()
#browser.get('http://www.baidu.com')
item = {
    'id':'10012',
    'traffic':"45'87",
    'play_time':"'''we",
    'sight':"['abc']",
    'open_time':"qw''er",
    'where':"qwqw''",
    'telephone':'aas',
    'ticket':"'[name]'"
}
class MafengwoPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='ddr4', db='mafengwo', port=3306)
        self.cursor = self.connect.cursor()


    def process_item(self):
        #db = pymysql.connect('localhost', 'root', 'ddr4', 'mafengwo')
        #point = db.cursor()#获取操作对象
        #组成sql语句
        id = item['id'].replace('\'', '')
        sight = item['sight'].replace('\'', '')
        telephone = item['telephone'].replace('\'', '')
        play_time = item['play_time'].replace('\'', '')
        ticket = item['ticket'].replace('\'', '')
        open_time = item['open_time'].replace('\'', '')
        traffic = item['traffic'].replace('\'', '')
        where = item['where'].replace('\'', '')
        sql = "insert into sight(id,sight,telephone,play_time,ticket,open_time, traffic, place) " \
              "values({},'{}','{}','{}','{}','{}','{}','{}')".format(int(id), sight, telephone,
                                                                     play_time, ticket, open_time,
                                                                     traffic, where)

        #point.excute(sql)
        try:

            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.connect.commit()
            print('handle on it!')
        except:
            # 如果发生错误则回滚
            self.connect.rollback()
            print('出错了！！')
        finally:
            self.cursor.close()
            self.connect.close()

m = MafengwoPipeline()
m.process_item()

'''http = ['http://47.94.249.125:11111','http://192.144.153.177:11111','http://188.131.204.14:12345']
proxy = random.choice(http)
def get_content():
    print(proxy)
    data = {
                'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
                'iMddid': str(10030),
                'iTagId': '0',
                'iPage': str(2),
                '_ts': '1555765965445',
                '_sn': '79de19dd77'}
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                'Referer': 'https://www.mafengwo.cn/jd/{}/gonglve.html'.format(str(10030)),
                'Host': 'www.mafengwo.cn'
            }
    #post_data = {'sAct':'KMdd_StructWebAjax|GetPoisByTag','iMddid':str(10030),'iTagId':'0','iPage':'1','_ts':'1555545267384','_sn':'02f4ee3c03'}
            #post请求，异步加载页面，iTagId是种类，这个用不到，iPage是页面，加载为0
    url = 'http://www.mafengwo.cn/ajax/router.php'
    resp = requests.post(url=url, headers=headers, data=data, verify=False)
    print(resp)
    return resp.text
print(get_content())'''