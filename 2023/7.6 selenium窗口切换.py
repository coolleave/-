from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
import time  # 导包
web = Edge()  # 创建浏览器
url = 'https://www.baidu.com/'
web.get(url)  # 打开浏览器
web.find_element('xpath', '//*[@id="kw"]').send_keys('平泉一中', Keys.ENTER)  # 输入关键字
time.sleep(1)  # 睡眠一秒给浏览器反应时间
web.find_element('xpath', '//*[@id="1"]/div/h3/a').click()  # 点击搜索结果
web.switch_to.window(web.window_handles[-1])  # 切换窗口到当前最后一个打开的窗口
# 找到详情页中的结果并返回
name = web.find_element('xpath', '/html/body/div[3]/div[2]/div/div[1]/dl[1]/dd/span[1]/h1').text
print(name)
web.close()  # 关闭当前子窗口
web.switch_to.window(web.window_handles[-1])  # 切换回原来的窗口
# 测试是否返回
result = web.find_element('xpath', '//*[@id="3"]/div/h3/a/div/div/p/span/span').text
print(result)
# 测试成功

