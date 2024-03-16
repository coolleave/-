import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

# 获取小说id及名称
def get_id():
    url = 'https://www.faloo.com/'
    resp = requests.get(url)
    # 用etree来处理
    tree = etree.HTML(resp.text)
    # 用xpath来定位li标签单元
    lis = tree.xpath('/html/body/div[9]/div[2]/ul/li')
    # 获取每一个单元的url和title
    tasks = []
    for li in lis:
        book_url = li.xpath('./a/@href')[0]
        book_title = li.xpath('./a/@title')[0]
        book_id = book_url.split('.')[-2].split('/')[-1]
        # 传入参数d
        with ThreadPoolExecutor(50) as t:
            t.submit(simple_dowload, book_id=book_id, name=book_title)


# 下载单个小说并保存为txt格式
def simple_dowload(book_id, name):
    for chapter in range(1, 70):
        url = f'https://b.faloo.com/{book_id}_{chapter}.html'
        resp = requests.get(url)
        # 生成用etree处理
        tree = etree.HTML(resp.text)
        # 通过xpath定位所有的标签
        text = tree.xpath("//div[@class='noveContent']//p/text()")
        with open(f'./txt/{name}.txt', mode='a', encoding='utf-8') as w:
            for i in text:
                w.write(i+'\n')  # 添加换行
            w.write('***************')  # 添加章节分隔符
        print(f'{name}第{chapter}章下载完毕')


if __name__ == '__main__':
    get_id()
