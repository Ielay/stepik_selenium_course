from selenium import webdriver
import time
import math 


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # достаём x
    input_val = browser.find_element_by_id("input_value")
    x = input_val.text
    y = calc(x)

    # пишем ответ
    answ_inp = browser.find_element_by_id("answer")
    answ_inp.send_keys(y)

    # checkbox
    checkbox = browser.find_element_by_css_selector(".form-check > #robotCheckbox")
    checkbox.click()

    # radiobutton
    radio = browser.find_element_by_css_selector(".form-check > #robotsRule")
    radio.click()

    # submit
    subm_btn = browser.find_element_by_css_selector("button[type='submit']")
    subm_btn.click()

    time.sleep(10)    

finally:
    time.sleep(30)
    browser.quit()

