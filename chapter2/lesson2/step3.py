from selenium import webdriver
import time
import math 


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text

    ans = int(num1) + int(num2)

    print("ANSWER: " + str(ans))

    # кликаем по селекту
    browser.find_element_by_id("dropdown").click()
    # выбираем конкретный ответ
    right_option_selector = "#dropdown > option[value='" + str(ans) + "']"
    print(right_option_selector)
    browser.find_element_by_css_selector(right_option_selector).click()
    
    # submit 
    browser.find_element_by_css_selector("button[type='submit']").click()
finally:
    time.sleep(30)
    browser.quit()

