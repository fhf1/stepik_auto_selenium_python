# При написании end-to-end тестов на Selenium могут возникать проблемы, называемые Flaky-тесты или "мигающие" авто-тесты,
# т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов, могут иногда падать,
# хотя всё остальное время они проходят успешно. Это может происходить в момент прохождения тестов
# из-за одновременного обновления сайта, из-за сетевых проблем или странных стечений обстоятельств.
# Конечно, надо стараться исключать такие проблемы и искать причины возникновения багов, но в реальном мире бывает, что это требует слишком много усилий.
# Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг, а не упал случайно.

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("magic_link")

# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py
# "--reruns n", где n — это количество перезапусков
# "--tb=line" - сократить лог с результатами теста