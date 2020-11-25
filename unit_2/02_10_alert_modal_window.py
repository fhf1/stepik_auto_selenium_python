# вариант с одной кнопкой ОК:
alert = browser.switch_to.alert
alert.accept()
# получить текст из alert
alert_text = alert.text

# вариант модального окна с двумя кнопками (ОК, Отмена):
confirm = browser.switch_to.alert
confirm.accept()
# для отказа:
confirm.dismiss()

# вариант с двумя кнопками и полем для ввода текста:
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
