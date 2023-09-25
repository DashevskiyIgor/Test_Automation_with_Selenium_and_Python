import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

browser.get(link)
browser.maximize_window()
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
window1 = browser.window_handles[0]
window2 = browser.window_handles[1]
browser.switch_to.window(window2)
x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
browser.switch_to.window(window1)
browser.switch_to.window(window2)
print(browser.switch_to.alert.text)


time.sleep(15)
browser.quit()
