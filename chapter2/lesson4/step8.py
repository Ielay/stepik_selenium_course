from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math 


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # btn
    book_btn = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_btn.click()
    
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

