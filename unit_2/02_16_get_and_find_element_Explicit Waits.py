from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # (здесь надо использовать поиск элементов с помощью класса By)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
    # element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
    
    # в объекте WebDriverWait используется функция until, в которую передается 
    # правило ожидания, элемент, а также значение, по которому мы будем искать элемент.
    
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
finally:
    time.sleep(5)
    browser.quit()

# ============================
# Дополнительно:
# говорим Selenium проверять в течение 5 секунд пока кнопка станет НЕактивной:

# button = WebDriverWait(browser, 5).until_not(
#     EC.element_to_be_clickable((By.ID, "verify"))
#     )
# ============================