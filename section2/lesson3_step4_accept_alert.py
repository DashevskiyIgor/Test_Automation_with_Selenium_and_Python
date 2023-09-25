import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
browser.switch_to.alert.accept()
x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()
