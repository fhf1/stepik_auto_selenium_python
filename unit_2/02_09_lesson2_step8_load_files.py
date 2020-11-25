from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    fname = browser.find_element_by_name("firstname")
    fname.send_keys("Vitaly")
    lname = browser.find_element_by_name("lastname")
    lname.send_keys("Vertyakov")
    e_mail = browser.find_element_by_name("email")
    e_mail.send_keys("vitaverty@gmail.com")
    # # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'test_load_file.txt')
    button_choose_file = browser.find_element_by_id("file")
    button_choose_file.send_keys(file_path)
    button_submit = browser.find_element_by_xpath('//button[@type="submit"]')
    button_submit.click()

finally:
    time.sleep(8)
    browser.quit()