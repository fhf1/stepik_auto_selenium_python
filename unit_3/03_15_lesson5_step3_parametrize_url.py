import time
import math
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("lesson", [
    '236895',
    '236896',
    '236897',
    '236898',
    '236899',
    '236903',
    '236904',
    '236905'
    ])
def test_guest_should_see_feedback_is_correct(browser, lesson):
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    # открываем страницу
    browser.get(link)
    # Ответ для каждой задачи пересчитываем отдельно, иначе они устаревают:
    answer = str(math.log(int(time.time())))
    input_answer = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "string-quiz__textarea"))
        )
    # вводим правильный ответ
    input_answer.send_keys(answer)

    button_send = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
    button_send.click()

    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__feedback"))
        )

    assert feedback.text == "Correct!", f'Текст в поле фидбек отличается от ожидаемого! \nОжидаемый результат: Correct!\nФактический результат: {feedback.text}'
