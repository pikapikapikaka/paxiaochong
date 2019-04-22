import random
import requests
http = ['http://47.94.249.125:11111','http://192.144.153.177:11111','http://188.131.204.14:12345']
def getpost(number,page):
    proxy = random.choice(http)
    data = {
                'sAct': 'KMdd_StructWebAjax|GetPoisByTag',
                'iMddid': str(number),
                'iTagId': '0',
                'iPage': str(page),
                '_ts': '1555765965445',
                '_sn': '79de19dd77'}
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                'Referer': 'https://www.mafengwo.cn/jd/{}/gonglve.html'.format(str(number)),
                'Host': 'www.mafengwo.cn'
            }
    #post_data = {'sAct':'KMdd_StructWebAjax|GetPoisByTag','iMddid':str(10030),'iTagId':'0','iPage':'1','_ts':'1555545267384','_sn':'02f4ee3c03'}
            #post请求，异步加载页面，iTagId是种类，这个用不到，iPage是页面，加载为0
    url = 'http://www.mafengwo.cn/ajax/router.php'
    resp = requests.post(url=url, headers=headers, data=data, proxies={'http': proxy}, verify=False)

    return resp.text