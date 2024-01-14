import requests
from lxml import etree
# 免费获取的代理ip 不一定都能用，因此我们要检验代理ip的可用性
params = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko)Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}


def check_proxy(proxy):
    try:
        resp = requests.get('http://www.baidu.com', proxies=proxy, timeout=5, params=params)
        if resp.status_code == 200:
            # print(f'{proxy}可用')
            lst_ip.append(proxy)

            return True
        else:
            return False
    except:
        return False

# 我们从网站上爬取一些ip代理。


# 通过免费代理网进行爬取ip，但代理网有反爬机制，失败！
def get_ip():
    headers = {'Cookie': 'channelid=0; sid=1705223609394396'}
    url = 'https://www.kuaidaili.com/free/intr'
    resp = requests.get(url, params=params, headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath('//*[@id="list"]/div[2]/table/tbody/tr')
    for tr in trs:
        ip = tr.xpath('./td[1]/text()')
        port = tr.xpath('./td[2]/text()')
        http = {'https': f'{ip}:{port}'}
        check_proxy(http)


# 启动plan B 从知乎上搜
def get_ip2():
    url = 'https://zhuanlan.zhihu.com/p/395461277'
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    ps = tree.xpath('//*[@id="root"]/div/main/div/article/div[1]/div/div/div/p')
    for p in ps:
        try:
            text = p.xpath('./text()')
            text = text[0]
            ip = text.split("[")[0]
            http = {'https//:': f'{ip}'}
            check_proxy(http)
        except:
            pass


if __name__ == '__main__':
    lst_ip = []
    get_ip2()
    for i in lst_ip:
        print(i)
    # resp1 = requests.get('https://zhuanlan.zhihu.com/p/395461277', params=params)
