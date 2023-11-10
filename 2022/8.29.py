# 导入模块
import requests
import re
import csv
from concurrent.futures import ThreadPoolExecutor
f = open('data.csv', mode='w', encoding='utf-8')
csv_writer = csv.writer(f)
head_lst = ['名称', '最低价', '最高价', '平均价']
csv_writer.writerow(head_lst)
"""
说明：这里 樵夫老师本来是用xpath进行演示的 但是因为经过了两年
    新发地的网址已经升级，菜价已经不在网页的源代码中，而是在二次请求中，所以我们改变了解析方法
    改变为re解析 这样就行了 并且实验成功 本来是练习线程池的操作 却变成了复习re。
 #  讲网址交给etree解析处理
    html = etree.HTML(resp.text)
    table = html.xpath('//*[@id="bbs"]/div/div/div/div[4]/div[1]/div/table')[0]
    trs = table.xpath('./tr')
    print(len(trs))
"""


def down_onepage(i):
    url1 = 'http://www.xinfadi.com.cn/getPriceData.html'
    dic = {'current': f'{i}'}
    resp1 = requests.post(url1, headers=dic)

    obj = re.compile(r'.*?prodName":"(?P<name>.*?)".*?lowPrice":"(?P<lowprice>.*?)".*?'
                     r'highPrice":"(?P<highprice>.*?)".*?avgPrice":"(?P<avgprice>.*?)"')
    result = obj.finditer(resp1.text)
    for i in result:
        name = i.group('name')
        low_price = i.group('lowprice')
        high_price = i.group('highprice')
        avg_price = i.group('avgprice')
        lst = [f'{name} ', f'{low_price}',
               f'{high_price}', f'{avg_price}']
        # print(lst)
        csv_writer.writerow(lst)
        print('over!')


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 100):
            t.submit(down_onepage(i))
            print(f'线程{i}')
