from datetime import datetime as dt
from selenium import webdriver
import time


# 定义一个时间字符串
time_str = "2024-06-10 13:14:30"

# 将时间字符串解析为 datetime 对象
time_obj = dt.strptime(time_str, "%Y-%m-%d %H:%M:%S")

browser = webdriver.Edge()
browser.get("https://www.taobao.com")
time.sleep(3)                               #点击
browser.find_element('xpath', "/html/body/div[3]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/a[1]").click()


print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)


while True:
    try:
        if browser.find_element('id', "J_SelectAll1"):
            browser.find_element('id', "J_SelectAll1").click()
            break
    except:
        print(f"找不到购买按钮")


while True:
    current_time = dt.now()
    print(current_time)
    #获取电脑现在的时间,year month day


    # 对比时间，时间到的话就点击结算


    #判断是不是到了秒杀时间?

    if current_time > time_obj:
        print("now!")

    #     # 点击结算按钮
        while True:
            try:
                if browser.find_element('link_text', "结 算"):
                    print("here")
                    browser.find_element('link_text', "结 算").click()
                    print(f"主人,程序锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element('link_text', '提交订单'):
                    browser.find_element('link_text', '提交订单')
                    print(f"抢购成功，请尽快付款")
            except:
                print(f"我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)
