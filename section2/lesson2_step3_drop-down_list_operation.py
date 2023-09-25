from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

browser.get(link)
browser.maximize_window()

x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
y = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
summa = x + y
Select(browser.find_element(By.TAG_NAME, 'select')).select_by_value(str(summa))
browser.find_element(By.CSS_SELECTOR, '[type=submit]').click()
print(browser.switch_to.alert.text)

time.sleep(5)
