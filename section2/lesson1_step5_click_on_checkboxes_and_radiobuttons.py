import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default').click()

time.sleep(20)
browser.quit()
