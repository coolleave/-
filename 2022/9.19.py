from selenium.webdriver import Edge
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By
import time


def pqyz():
    web = Edge()  # 创建浏览器
    web.get('http://121.26.242.250:8001/srcja.asp?dhhm1=aaaa')
    # 处理验证码
    print('正在处理验证码')
    img = web.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[4]/div/font/img').screenshot_as_png
    chaojiying = Chaojiying_Client('coolleave', '2855048477.y', '939148')
    code_dic = chaojiying.PostPic(img, 1004)
    code = code_dic['pic_str']
    print('处理完成')

    # 输入用户名 密码 验证码
    print('正在输入相关数据')
    web.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[1]/div/font/input').send_keys('王文杰')
    web.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/div/font/input').send_keys('wwjwangwenjie1')
    web.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[3]/div/font/input').send_keys(code)
    # 点击提交
    time.sleep(5)
    web.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[5]/div/font/input[1]').click()
    time.sleep(5)  # 睡上5秒钟观察
    print('完成！')


def xk():
    web = Edge()
    web.get('https://xk.hebeea.edu.cn/register/#/login')
    # 处理验证码
    print('正在处理验证码')
    img = web.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[3]/div/div/div[2]/img').screenshot_as_png
    chaojiying = Chaojiying_Client('coolleave', '2855048477.y', '939148')
    code_dic = chaojiying.PostPic(img, 1004)
    code = code_dic['pic_str']
    print('解析成功！')
    print('正在输入相关数据')
    # 输入用户名密码验证码
    web.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[1]/div/div/input').send_keys('210823012231')
    web.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[2]/div/div/input').send_keys('Cpy250')
    web.find_element(By.XPATH, '//*[@id="pane-account"]/form/div[3]/div/div/div[1]/div/input').send_keys(code)
    print('输入成功！')
    time.sleep(3)
    # 点击
    web.find_element(By.XPATH, '//*[@id="app"]/section/main/div/div/div/div[2]/button').click()
    print('登录完成！')
    time.sleep(10)


xk()
