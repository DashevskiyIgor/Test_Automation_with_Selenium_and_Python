from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)
valuex = browser.find_element(By.CSS_SELECTOR, 'img').get_attribute('valuex')
res = calc(valuex)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(res)
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
time.sleep(20)
browser.quit()
