from selenium import webdriver
import time
import math 


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # press the btn
    troll_btn = browser.find_element_by_css_selector(".container > button.trollface[type='submit']")
    troll_btn.click()
    
    # switch the window
    browser.switch_to_window(browser.window_handles[1])
    
    # достаём x
    input_val = browser.find_element_by_id("input_value")
    x = input_val.text
    y = calc(x)

    # пишем ответ
    answ_inp = browser.find_element_by_id("answer")
    answ_inp.send_keys(y)
    
    # submit
    subm_btn = browser.find_element_by_css_selector("button[type='submit']")
    subm_btn.click()

    time.sleep(10)    

finally:
    time.sleep(30)
    browser.quit()

