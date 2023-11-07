from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
import time
import requests

url = 'https://www.kongfz.com/'


def sel():
    web = Edge()
    web.get(url)
    time.sleep(2)
    id = 9787576037753
    web.find_element('xpath', '//*[@id="searchInput"]').send_keys(id, Keys.ENTER)
    time.sleep(2)
    divs = web.find_elements('xpath', '//*[@id="listBox"]/div')
    for div in divs:
        name = div.find_element('xpath', './div[2]/div[1]/a').text
        price = div.find_element('xpath', './div[3]/div[1]/div[2]/span[2]').text
        send_price = div.find_element('xpath', './div[3]/div[3]/div/span[2]').text
        print(name, price, send_price)


def re():
    resp = requests.get(url)
    print(resp)


if __name__ == '__main__':
    re()