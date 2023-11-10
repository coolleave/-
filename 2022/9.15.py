#  全新模块 selenium
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By  # 导入by解析包
from selenium.webdriver.common.keys import Keys  # 导入按键包
import time

web = Edge()  # 创建一个浏览器
url = 'http://121.26.242.250:8001/cxxsyzxha.asp'
web.get(url)  # 打开浏览器对应的网址

print(web.title)

el1 = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/font/input[2]')
el1.click()  # 点击
time.sleep(1)  # 防止网页还没来得及刷新就执行了下一个操作，所以在这里睡上一秒
# 找到输入框 并且输入内容 并且输入回车
web.find_element(By.XPATH, '//*[@id="xma"]').send_keys('陈鹏宇', Keys.ENTER)
# 这里直接输入换行符号'/n'也是可以的
