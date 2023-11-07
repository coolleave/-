from chaojiying import Chaojiying_Client
from selenium.webdriver import Edge
import time
# 创建浏览器并打开
web = Edge()
web.get('https://www.chaojiying.com/user/login/')
# 定位储存图片（用screenshot的方式）
img = web.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

# 调出超级鹰程序
chaojiying = Chaojiying_Client('coolleave', '2855048477.y', '939148')  # 输入账号密码
dic = chaojiying.PostPic(img, 1902)  # 输入需要识别的图片验证码
code = dic['pic_str']  # 输入验证码

# 输入账号密码验证码
web.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('coolleave')
web.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('2855048477.y')
web.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code)
time.sleep(3)  # 停留几秒
# 点击登录
web.find_element('xpath', '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
time.sleep(10)
