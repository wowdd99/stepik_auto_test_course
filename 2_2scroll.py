from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    #ввод значений в поле ввода 
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    #скролл
    button = browser.find_element(By.XPATH, "//button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    #чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotcheckbox")
    option1.click()
    
    #радиобатн
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()   
                                  
    #нажать кнопку
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

