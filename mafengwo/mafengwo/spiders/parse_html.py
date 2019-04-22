import re
from bs4 import BeautifulSoup

def parse_sight_comment(sentence):
    #print('sentence:',sentence)
    res = sentence.split('<div class="loading-img" style="display: none;">')[0]#此标签地下都是评论，故去除，免得影响性能
    #content = res.encode('utf-8', 'ignore').decode()#其中内容是/u6874,不是汉子，不方便操作
    #content = content.replace('\/', '/')#原来的‘/’都变成了'\/'
    result = re.search('(jQuery\d*_\d*)', res)#将开头的jQuery...去掉
    # print(result.group(0))
    data = res[len(result.group(0)) + 1:len(res) - 2]  # 获取到字典类型的数据
    data = eval(data)#将字符串转化为字典
    # print(data['data']['html'])
    result = data['data']['html'].encode('utf8', 'ignore').decode()#将其中的内容可读化
    result = result.replace('\/', '/')  # replace会返回一个新的字符串
    # print(result)
    bs = BeautifulSoup(result, 'html.parser')#调用bs进行解析
    # bs.find('div', class_='mod mod-reviews')
    div = bs.find_all('a', href='javascript:void(0);')  # 找到所有的评价
    # print(type(div[0]))#类型是Tag
    # print(div)
    d = {}#将产生的评价数量放到字典中，0代表好评，1中评，2差评
    for i in div:#从头向后遍历
        # comment = BeautifulSoup(i, 'html.parser')
        comment = i.find_all('span')  # 返回span的列表，评论标签都在这个列表里
        for i in range(len(comment)):
            # print(comment[i])
            # origin = comment[i + 1]
            if '好评' in comment[i]:#分析其结构发现，若i对应着“好评”，那么i+1对应着好评的数量
                origin = str(comment[i + 1])#将其转换成str类型
                #print(origin)
                #print(type(origin))
                zhengze = re.search('\d*条', origin)#若不加“条”，找不到对应的结果，原理不是很清楚
                #print(zhengze)
                num = zhengze.group(0)#得到最终结果
                d[0] = num
            elif '中评' in comment[i]:
                origin = str(comment[i + 1])
                zhengze = re.search('\d*条', origin)
                num = zhengze.group(0)
                d[1] = num
            elif '差评' in comment[i]:
                origin = str(comment[i + 1])
                zhengze = re.search('\d*条', origin)
                num = zhengze.group(0)
                d[2] = num
    return d#将结果返回