import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
browser.find_element(By.XPATH, '//*[@id="book"]').click()
submit_button = browser.find_element(By.ID, 'solve')
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(calc(x))
submit_button.click()
print(browser.switch_to.alert.text)

time.sleep(5)
browser.quit()
