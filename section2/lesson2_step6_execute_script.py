import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

browser.get(link)
x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
radio_button = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()
button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
print(browser.switch_to.alert.text)
time.sleep(10)
browser.quit()
