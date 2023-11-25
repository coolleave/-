from selenium.webdriver import Edge
import time  # 导包
web = Edge()  # 创建浏览器


url = 'https://kns.cnki.net/kns8s/defaultresult/' \
      'index?crossids=YSTT4HG0%2CLSTPFY1C%2CJUP3MUPD%2CMPMFIG1A%2CWQ0UVIAA%2CBLZOG7CK%2CEMRPGLPA%' \
      '2CPWFIRAGL%2CNLBO1Z6R%2CNN3FJMUV&korder=' \
      'SU&kw=%E7%94%B2%E9%AA%A8%E6%96%87'

web.get(url)  # 打开浏览器
time.sleep(1)
button = web.find_element('xpath', '//*[@id="divGroup"]/dl[1]/dd[1]/div/ul/li[1]/input')  # 用xpath找到按钮元素
button.click()  # 点击事件
time.sleep(2)
for i in range(15):
    # print(elements)
    elements = web.find_elements('xpath', '//*[@id="gridTable"]/div/div/table/tbody/tr')  # 找到单元框
    try:
        for element in elements:
                    name = element.find_element('xpath', './td[2]/a').text   # 每个单元的名称
                    author = element.find_element('xpath', './td[3]/a[1]').text  # 每个单元的作者
                    journal = element.find_element('xpath', './td[4]/p/a').text  # 每个单元的来源
                    time = element.find_element('xpath', './td[5]').text  # 每个单元的时间
                    print(f"{author} 《{name}》, 《{journal}》, {time}")
    except:
        pass
    finally:
        button1 = web.find_element('xpath', '//*[@id="PageNext"]')
        button1.click()
        a = input(" ")

