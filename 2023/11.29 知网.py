from selenium.webdriver import Edge
import time  # 导包
web = Edge()  # 创建浏览器
url = 'https://kns.cnki.net/kns8s/defaultresult/' \
      'index?crossids=YSTT4HG0%2CLSTPFY1C%2CJUP3MUPD%2CMPMFIG1A%2CWQ0UVIAA%' \
      '2CBLZOG7CK%2CEMRPGLPA%2CPWFIRAGL%2CNLBO1Z6R%2CNN3FJMUV&korder=SU' \
      '&kw=%E7%94%B2%E9%AA%A8%E6%96%87'

web.get(url)  # 打开浏览器
time.sleep(1)  # 等待浏览器响应一秒

button = web.find_element('xpath', '//*[@id="ModuleSearch"]/div[2]/div/div/ul/li[1]/a')
button.click()  # 点击学术期刊按钮
time.sleep(2)
button1 = web.find_element('xpath', '//*[@id="DivDisplayMode"]/li[1]')
button1.click()  # 点击列表模式
time.sleep(3)
for i in range(15):
    a = input("")
    elements = web.find_elements('xpath', '//*[@id="gridTable"]/div/div/dl/dd')
    for element in elements:
        try:
            name = element.find_element('xpath', './div[2]/h6/a').text  # 名称
            author = element.find_element('xpath', './div[2]/div/p/a').text  # 作者名称
            time = element.find_element('xpath', './div[2]/p[1]/span[1]/a').text  # 报纸名称
            journal = element.find_element('xpath', './div[2]/p[1]/span[2]/a').text  # 期刊时间
            print(f'{author}，《{name}》，《{time}》，{journal}')
        except:
            pass
    button2 = web.find_element('xpath', '//*[@id="PageNext"]')  # 寻找下一页
    button2.click()
