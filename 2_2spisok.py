from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #найдем первую цифру
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = num1.text
    #найдем вторуюю цифру
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = num2.text

    import math

    def calc():
        z = str(int(x) + int(y))
        return z
    z = calc()
                                  
    #ищем элемент из списка
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
