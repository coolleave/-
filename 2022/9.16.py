# 今天继续学习selenium
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time


def name():
    url = 'http://121.26.242.250:8001/cxxsa.asp'
    web = Edge()  # 创建一个浏览器
    web.get(url)
    # 找到浏览器的元素
    submit = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/font/input[2]')
    submit.click()  # 点击浏览器
    # /html/body/form/table/tbody/tr[3]/td/div/select/option[39]
    # 选择所需要的选项
    class_i = web.find_element(By.XPATH, f'/html/body/form/table/tbody/tr[3]/td/div/select/option[149]')
    time.sleep(4)
    class_i.click()  # 点击
    message = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/input[1]')
    message.click()
    for i in range(3, 200, 5):
        names = web.find_element(By.XPATH, f'/html/body/div/table/tbody/tr[{i}]')
        name1 = names.find_element(By.XPATH, './td[4]/font/a').text  # 输出文本
        print(name1)


def tb():
    web = Edge()
    url = 'https://www.taobao.com/'
    web.get(url)
    time.sleep(3)
    web.find_element(By.XPATH, '//*[@id="q"]').send_keys('行李箱')  # 输入内容
    butten = web.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')
    butten.click()


if __name__ == '__main__':
    name()