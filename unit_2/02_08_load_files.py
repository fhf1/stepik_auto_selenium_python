import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')
element.send_keys(file_path)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

# Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
# Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path).

# =========================
# Допустим, мы написали код скрипта и сохранили код в lesson2_step7.py в свой локальной папкеD:\stepik_homework.
# Активируем виртуальное окружение и запускаем его python lesson2_step7.py
# В таком случае конструкция os.path.abspath(os.path.dirname(__file__)) вернет нам путь до директории файла с кодом, то есть D:\stepik_homework.
# В эту же папку кладем файл, который хотим прикрепить, то есть file.txt. Тогда, после выполнения команды:
# file_path = os.path.join(current_dir, 'file.txt')
# В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'.
# Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt
# перенесем в другую папку, или на компьютер с другой ОС, то такой код без правок заработает и там. 
# ===========================