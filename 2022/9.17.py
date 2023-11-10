from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time
web = Edge()


def lg():
    url = 'https://www.lagou.com/'
    web.get(url)
    qg = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
    qg.click()
    web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', '\n')  # 正常
    time.sleep(1)  # //*[@id="jobList"]/div[1]
    elements = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
    time.sleep(3)
    for element in elements:
        name = element.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text
        salary = element.find_element(By.XPATH, '.div[1]/div[1]/div[2]/span').text
        company = element.find_element(By.XPATH, './div[1]/div[2]/div[1]').text
        request = element.find_element(By.XPATH, './div[1]/div[1]/div[2]').text
        print(name, salary, company, request)


# def switch():
#     web.switch_to.window(web.window_handles[0])


if __name__ == '__main__':
    lg()
