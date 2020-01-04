from selenium import webdriver
import time
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет обязательные поля
    f_name_inp = browser.find_element_by_css_selector('input[name="firstname"]')
    f_name_inp.send_keys("Jerry")

    s_name_inp = browser.find_element_by_css_selector('input[name="lastname"]')
    s_name_inp.send_keys("Smith")

    email_inp = browser.find_element_by_css_selector('input[name="email"]')
    email_inp.send_keys("jerry_smith@gmail.com")
    
    # загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'sample.txt')           # добавляем к этому пути имя файла 
    load_file_elem = browser.find_element_by_css_selector("#file")
    load_file_elem.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)
	
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
	
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()


