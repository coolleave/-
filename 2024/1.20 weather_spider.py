import aiohttp
import asyncio
import csv
from lxml import etree


# 准备ua
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}


# 定义单个下载文件函数
async def download(url):
    month_lst = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            text = await resp.text()
            tree = etree.HTML(text)
            lis = tree.xpath('/html/body/div[7]/div[1]/div[4]/ul/li')
            for li in lis:
                day_dic = {}
                date = li.xpath('./div[1]/text()')[0].split(' ')[0]
                high = li.xpath('./div[2]/text()')[0].replace('℃', '')
                low = li.xpath('./div[3]/text()')[0].replace('℃', '')
                weather = li.xpath('./div[4]/text()')[0]
                wind = li.xpath('./div[5]/text()')[0]
                # print(date, high, low, weather, wind)
                day_dic['date'] = date
                day_dic['high'] = high
                day_dic['low'] = low
                day_dic['wind'] = str(wind)
                month_lst.append(day_dic)
    weathers.append(month_lst)


# 获取处理获取url函数
async def get_url():
    tasks = []
    for i in range(1, 13):
        # 使用三目操作符处理日期
        date = '0' + str(i) if i < 10 else str(i)
        # print(date)
        url = f'https://lishi.tianqi.com/pingquan/2023{date}.html'
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    weathers = []

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_url())
    # print(weathers)
    with open('weather.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # 写入列名
        writer.writerow(['日期', '最高气温', '最低气温', '天气', '风向'])
        # writer.writerows(list(value) for month in weathers for day in month for key, value in day.items())
        # print([list(value) for month in weathers for day in month for key, value in day.items()])

        for month in weathers:
            # print(month, type(month))
            for day in month:
                # print(day, type(day))
                lst = []
                for key, value in day.items():
                    lst.append(value)
                # print(lst)
                writer.writerow(lst)
