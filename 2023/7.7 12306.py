from selenium.webdriver import Edge
from chaojiying import Chaojiying_Client
import time
from selenium.webdriver.common.action_chains import ActionChains  # 导入移动鼠标包
from selenium.webdriver.edge.options import Options  # 导入选项包，用于无头浏览器和反爬


def click():
    # 创建浏览器
    url = 'https://dun.163.com/trial/picture-click'
    # 这是非常重要的去除浏览器自动化测试的方法
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')

    web = Edge(options=option)
    web.get(url)
    # 初始化
    web.maximize_window()
    web.find_element('xpath', '/html/body/main/div[1]/div/div[2]/div[2]/ul/li[2]').click()
    time.sleep(3)
    #  找到验证码
    pic = web.find_element('xpath',  '/html/body/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]'
                                     '/div[3]/div/div/div[1]/div/div[1]/img[1]')
    chaojiying_com(web, pic)


def chaojiying_com(web, pic):
    # 用超级鹰处理验证码
    chaojiying = Chaojiying_Client('coolleave', '2855048477.y', '939148')
    dic = chaojiying.PostPic(pic.screenshot_as_png, 9501)
    print(dic['pic_str'])
    # 接受返回值并且对返回值切割处理
    locates = dic['pic_str'].split('|')
    # 找出每个点的xy坐标
    for locate in locates:
        loc1 = locate.split(',')
        x = int(loc1[1])  # 返回值为字符串，格式化为整型
        y = int(loc1[2])
        print(x, y)
        ActionChains(web).reset_actions()
        # 移动xy位置并且点击，注意pic作为原点，xy为相对坐标。并且后边必须有perform才能执行
        time.sleep(5)
        ActionChains(web).move_to_element_with_offset(pic, x, y).click().perform()
        print(f'{loc1[0]}点击完毕！')

        time.sleep(20)


def click1():  # 失败 未能通过网站的智能检测
    url = 'https://www.geetest.com/adaptive-captcha-demo'
    web = Edge()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'}
    web.get(url)
    time.sleep(2)
    web.find_element('xpath', '//*[@id="gt-showZh-mobile"]/div/section/div/div[2]/div[1]/div[2]/div[3]/div[4]').click()
    time.sleep(0.5)
    web.find_element('xpath', '//*[@id="captcha"]/div[2]/div[1]/div[1]').click()
    time.sleep(0.5)
    pic = web.find_element('xpath', '//*[@id="captcha"]/div[2]/div[1]/div[4]/div[1]/div[2]/div/div/div[1]/div[1]')
    chaojiying_com(web, pic)


def g12306():  # 代码完美执行
    url = 'https://www.12306.cn/index/'
    # 反爬
    option = Options()
    option.add_argument('--disable-blink-features=AutomationControlled')
    web = Edge(options=option)
    web.get(url)
    # 找到登录入口
    web.find_element('xpath', '//*[@id="J-btn-login"]').click()
    time.sleep(1)
    # 输入用户名密码点击登录
    web.find_element('xpath', '//*[@id="J-userName"]').send_keys('232323232')
    web.find_element('xpath', '//*[@id="J-password"]').send_keys('fd32999')
    web.find_element('xpath', '//*[@id="J-login"]').click()
    time.sleep(2)
    # 找到拖拽按钮
    btn = web.find_element('xpath', '//*[@id="nc_1_n1z"]')
    # 横向拖拽300个单位
    ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()


if __name__ == '__main__':
    g12306()

