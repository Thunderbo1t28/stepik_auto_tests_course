import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='firstname']")
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='lastname']")
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.CSS_SELECTOR, "div.form-group input[name='email']")
    input3.send_keys('Ivanivanov@gmai.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    input4 = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()