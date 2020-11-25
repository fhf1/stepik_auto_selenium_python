from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    req_input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    req_input1.send_keys("Vitaly")
    req_input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    req_input2.send_keys("Vertyakov")
    req_input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    req_input3.send_keys("vitaverty@gmail.com")
       
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # метод time.sleep(2), чтобы дождаться загрузки следующей страницы, прежде чем выполнять проверки.
    # Без использования такой паузы WebDriver может перейти к поиску тега h1 слишком рано, когда новая страница еще не загрузилась.
    # В таком случаем будем видеть в терминале ошибку:
    # NoSuchElementException... Unable to locate element: {"method":"tag name","selector":"h1"}
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Если результат проверки "Поздравляем! Вы успешно зарегистрировались!" == welcome_text вернет значение False, то далее выполнится код assert False.
# Он бросит исключение AssertionError и номер строки, в которой произошла ошибка.
# Если код написан правильно и работал ранее, то такой результат равносилен тому, что наш автотест обнаружил баг в тестируемом веб-приложении.
# 
# Если результат проверки вернет True, то выполнится выражение assert True. В этом случае код завершится без ошибок — тест прошел успешно.