from selenium.webdriver import Edge
import time
from selenium.webdriver.support.select import Select  # 导入select包
from selenium.webdriver.edge.options import Options  # 导入无头浏览器的包
opt = Options()  # options参数
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')


url = 'http://121.26.242.250:8001/cxxsa.asp'
web = Edge(options=opt)  # 将options参数传入
web.get(url)
# 点击提交
web.find_element('xpath', '/html/body/form/table/tbody/tr[4]/td/div/font/input[2]').click()
# 找到下来菜单元素并且包装成Select格式
sel = Select(web.find_element('xpath', '/html/body/form/table/tbody/tr[3]/td/div/select'))
for i in range(len(sel.options)):  # 利用索引顺序进行查找
    sel.select_by_index(i)
    time.sleep(2)
for i in range(111, 130):  # 利用value进行查找
    sel.select_by_value(i)
for i in range(1, 30):
    sel.select_by_visible_text(f'应届1年级{i}班')  # 利用文本内容进行查找
web.close()
