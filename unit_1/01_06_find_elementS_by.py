#... (импорты и т.д)

# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# Если метод find_element_by не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, которая прервёт выполнение кода.

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements_by_css_selector(".good")

# Метод find_elements_by всегда возвращает валидный результат: 
# если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.

# проверяем, что количество товаров равно 2
assert len(goods) == 2
