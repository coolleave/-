import requests
from bs4 import BeautifulSoup
import csv
for i in range(205500, 206000):
    url = f'http://121.26.242.250:8001/jxsxsxx.asp?yzxh={i}&nj=3'
    resp = requests.get(url)
    resp.encoding = 'gbk'
    # print(resp.text)
    page = BeautifulSoup(resp.text, 'html.parser')
    table = page.find('table')
    # print(table)
    try:
        name = table.find_all('div', align="center")[2].text
        xh = table.find_all('b',)[3].text.strip()
        xk = table.find_all('font', size=3)[2].text
        address = table.find_all('div', align="left")[3].text
        f = open('信息补充.csv', mode='a+')
        csv_writer = csv.writer(f)
        csv_writer.writerow([name, xh, xk, address])
        print(name, xh, xk, address)
        resp.close()
    except:
        resp.close()
        print(i)
