from selenium.webdriver import Edge
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

web = Edge()  # 创建一个浏览器
web.get('http://121.26.242.250:8001/cxxsa.asp')
# 点击提交
time.sleep(1)
web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/font/input[2]').click()
# 扎到select
sel_el = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[3]/td/div/select')
sel = Select(sel_el)  # 把元素包装select
# for i in range(len(sel.options)):  # 在select的范围内循环
c = 1
for i in range(1, 11):  # 在select的范围内循环
    # 扎到select
    sel_el = web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[3]/td/div/select')
    sel = Select(sel_el)  # 把元素包装select
    # for i in range(len(sel.options)):  # 在select的范围内循环

    sel.select_by_index(i)  # 在索引中查找
    # 点击学生信息，进入信息画面
    web.find_element(By.XPATH, '/html/body/form/table/tbody/tr[4]/td/div/input[1]').click()
    # 找到信息并输出
    time.sleep(2)

    print(f'{c}班名单')
    for b in range(3, 500, 5):
        # /html/body/div/table/tbody/tr[3]/td[4]/font/a
        # name = web.find_element(By.XPATH, f'/html/body/div/table/tbody/tr[{i}]')
        # resp = web.find_element(By.XPATH, './td[4]/font').text
        names = web.find_element(By.XPATH, f'/html/body/div/table/tbody/tr[{b}]/td[4]/font/a').text
        print(names,  end=' ')
    print('=================================================================')
    c += 1
    web.find_element(By.XPATH, '/html/body/div/table/tbody/tr[1]/td/div/font/a').click()
    time.sleep(1)

print('完成！')
