from selenium.webdriver import Edge  # 导入浏览器包
from selenium.webdriver.common.keys import Keys  # 导入热键包，可以ctrl加右键查看热键代码
import time
url = 'https://www.lagou.com/'  # 准备url
web = Edge()  # 创建浏览器，并不是打开浏览器
web.get(url)  # 打开浏览器
time.sleep(1)
button = web.find_element('xpath', '//*[@id="changeCityBox"]/ul/li[3]/a')  # 用xpath找到按钮元素
button.click()  # 点击事件
# 找到搜索框，并且输入内容和回车热键
'''
/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]
/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]
wage
/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/span/div/div[2]/span
/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[2]/span
company_name
/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a
'''
web.find_element('xpath', '//*[@id="search_input"]').send_keys('ps', Keys.ENTER)
elements = web.find_elements('xpath', '/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')  # 找到单元框
time.sleep(1)

for element in elements:
    name = element.find_element('xpath', '//*[@id="openWinPostion"]').text  # 每个职位的名称
    company_name = element.find_element('xpath', './div[1]/div[2]/div[1]/a').text  # 公司名字
    wage = element.find_element('xpath', './div[1]/div[1]/div[2]/span').text  # 薪资情况
    print(name, wage, company_name)
