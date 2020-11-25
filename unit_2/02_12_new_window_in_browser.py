# явно указать, на какую вкладку мы хотим перейти
browser.switch_to.window(window_name)

# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
# Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
new_window = browser.window_handles[1]

# запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
first_window = browser.window_handles[0]
# или:
current_window = browser.current_window_handle