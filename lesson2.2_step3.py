import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
  return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#num1")
    x = x_element.text

    y_element = browser.find_element(By.CSS_SELECTOR, "span#num2")
    y = y_element.text

    res = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    option1 = select.select_by_value(f"{res}")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()