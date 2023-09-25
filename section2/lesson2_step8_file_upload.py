import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser = webdriver.Chrome()

browser.get(link)
browser.find_element(By.CSS_SELECTOR, '[name=firstname]').send_keys('name')
browser.find_element(By.CSS_SELECTOR, '[name=lastname]').send_keys('last name')
browser.find_element(By.CSS_SELECTOR, '[name=email]').send_keys('email')
browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
print(browser.switch_to.alert.text)

time.sleep(15)
browser.quit()
