import rarfile
import requests
from lxml import etree
import random
import os
import re
import xlwt
from concurrent.futures import ThreadPoolExecutor


# 准备ua
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}

lst_ip = []  # 准备代理列表


# 通过知乎网页获取可用的代理ip
def get_ip2():
    url = 'https://zhuanlan.zhihu.com/p/395461277'
    resp = requests.get(url)
    tree = etree.HTML(resp.text)  # xpath 封装
    # xpath定位所有的p标签
    ps = tree.xpath('//*[@id="root"]/div/main/div/article/div[1]/div/div/div/p')
    for p in ps:
        try:
            text = p.xpath('./text()')  # 提取下载链接
            text = text[0]
            ip = text.split("[")[0]
            http = {'https//:': f'{ip}'}  # 拼接ip
            check_proxy(http)
        except:
            pass


# 检查代理ip是否可用
def check_proxy(proxy):
    try:
        # 访问百度，进行检查
        resp = requests.get('http://www.baidu.com', proxies=proxy, timeout=5)
        if resp.status_code == 200:
            # print(f'{proxy}可用')
            lst_ip.append(proxy)  # ip可用，将此ip添加到ip池当中
            return True
        else:
            return False
    except:
        return False


# 从主页找到所有的下载链接
def get_urls():
    for a in range(3, 7):
        url = f'http://www.12z.cn/book/wuxiaxianxia/list_13_{a}.html'
        # 发送GET请求获取页面内容，从代理池中使用随机ip
        resp = requests.get(url, headers=headers, proxies=random.choice(lst_ip))
        print(resp)
        resp.encoding = 'gbk'
        # 使用lxml解析页面内容
        html = etree.HTML(resp.text)
        # print(resp.text)
        # XPath所有的小说的链接/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a
        divs = html.xpath('/html/body/div[5]/div[2]/div[3]/div/div[1]/div')
        # print(urls)
        # 遍历所有的单元div
        with ThreadPoolExecutor(8) as t:
            for div in divs:
                # 找到进入小说详情页的href
                href = div.xpath('./div[1]/div[2]/div[1]/a/@href')
                t.submit(download, href[0])


# 下载单个rar文件
def download(url):
    resp = requests.get('http://www.12z.cn' + url, headers=headers, proxies=random.choice(lst_ip))  # 发送请求
    resp.encoding = 'gbk'  # 处理编码
    html = etree.HTML(resp.text)  # 用etree 封装网页
    download_url = html.xpath('//*[@id="djxz"]/div[2]/div[1]/div[1]/div[2]/ul/li[1]/a/@href')  # 通过xpath定位下载链接
    name = html.xpath('/html/body/div[5]/div/div[1]/div/div[1]/text()')  # 通过xpath找到小说名字

    # 保存文件
    with open(f'./rar/{name[0]}.rar', 'wb') as w:
        w.write(requests.get('http://www.12z.cn' + download_url[0], headers=headers).content)  # 下载文件
        print(f'成功下载文件{name[0]}')


# 解压当前文件夹下所有的压缩文件
def unzips(folder_path):
    for file_name in os.listdir(folder_path):  # 遍历文件夹内所有的文件
        if file_name.endswith('.rar'):  # 找到rar文件
            file_path = os.path.join(folder_path, file_name)
            # 解压找到的文件
            with rarfile.RarFile(file_path, 'r') as rf:
                rf.extractall('./txt')  # 解压到txt文件夹中


def novelchapters2(book_name):
    # 创建 Workbook 对象
    wb = xlwt.Workbook()
    # 创建工作表
    ws = wb.add_sheet('Sheet1')
    # print(f'{book_name}.txt')
    # 打开小说文件
    with open(f'./txt/{book_name}.txt', 'r', encoding='gb18030') as r:
        txt = r.read()
        lst = txt.split('\n\n')  # 用双换行符切
        # 写入表格
        a = 0
        for i in range(1, len(lst)):
            lst[i] = re.sub('.*?第.*?章.*', '', lst[i])  # 去掉卷标题
            lst[i] = re.sub('.*?第.*?卷.*', '', lst[i])  # 去掉章标题
            lst[i] = re.sub('\n\n\n', '\n\n', lst[i], flags=re.DOTALL)
            lst[i] = re.sub('\n\n', '', lst[i], flags=re.DOTALL)  # 去掉开头双换行符
            lst[i] = re.sub('\n', r'\\n', lst[i], flags=re.DOTALL)  # 把换行符替换成\n
            lst[i] = re.sub(r'\s\s', r'', lst[i], flags=re.DOTALL)  # 把换行符替换成\n
            # print(lst[1])
            # worksheet.cell(row=i, column=1, value=lst[i])
            if lst[i] == '\\n' or lst[i].startswith('内容简介') or lst[i].startswith('\\n内容简介'):
                a += 1
            else:
                ws.write(i-1-a, 0, lst[i])

        # 保存表格
        # workbook.save('novelchapters.xlsx')
        wb.save(f'./excel/{book_name}.xls')
        print(f'{book_name} over!')


# 找到txt文件名称，并传入章节处理函数
def handle_txt(folder_path):
    for file_name in os.listdir(folder_path):  # 遍历文件夹内所有的文件
        if file_name.endswith('.txt'):  # 找到txt文件名称
            file_name = file_name.split('.')[0]  # 切走后缀
            print(file_name)
            novelchapters2(file_name)


if __name__ == '__main__':
    # os.mkdir('rar')
    # os.mkdir('txt')
    # os.mkdir('excel')
    get_ip2()  # 拿到代理ip池
    # print(lst_ip)
    get_urls()  # 拿到并下载rar文件
    # unzips('./rar')  # 解压文件
    # handle_txt('./txt')  # 处理小说章节， 并写入excel
