from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_magic = browser.find_element_by_xpath("//button[@type='submit']")
    button_magic.click()
    # работаем с модальным окном
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button_submit = browser.find_element_by_xpath("//button[@type='submit']")
    button_submit.click()
finally:
    time.sleep(7)
    browser.quit()
