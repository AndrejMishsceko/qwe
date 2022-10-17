# Задание в группах: Создать телефонный справочник с возможностью импорта
# и экспорта данных в нескольких форматах.

import os
from PhoneBook import PhoneBook


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def input_int(msg=""):
    while True:
        try:
            result = int(input(msg))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result


def main_menu():
    # cls()
    global finish
    print('Добро пожаловать в телефонный справочник')
    print('Введите номер операции:')
    print('Показать все записи справочника - 1')
    print('Показать запись по номеру - 2')
    print('Найти запись по ФИО - 3')
    print('Найти запись по телефону - 4')
    print('Добавить запись в справочник - 5')
    print('Удалить запись по номеру - 6')
    print('Экспорт в файл - 7')
    print('Импорт из файла - 8')
    print('Сбросить (удалить все записи) - 9')
    print('Выход - 0')
    option = input_int()
    if option == 1:
        book.get_all()
        input("Нажмите Enter для продолжения...")
    elif option == 2:
        book.get(input_int("Введите номер записи для поиска: "))
        input("Нажмите Enter для продолжения...")
    elif option == 3:
        book.find("name", input("Введите часть ФИО: "))
        input("Нажмите Enter для продолжения...")
    elif option == 4:
        book.find("phone", input("Введите часть телефона: "))
        input("Нажмите Enter для продолжения...")
    elif option == 5:
        record = {}
        record['name'] = input("Введите ФИО: ")
        record['phone'] = input("Введите телефон: ")
        book.add(record)
        input("Нажмите Enter для продолжения...")
    elif option == 6:
        book.delete(input_int("Введите номер записи для удаления: "))
        input("Нажмите Enter для продолжения...")
    elif option == 7:
        print('Выберите тип файла для загрузки:')
        print('JSON - 1')
        print('CSV - 2')
        filetype = None
        while filetype == None:
            filetype = input_int()
            if filetype == 1:
                book.export(input("Введите имя файла для выгрузки: "), type='json')
            elif filetype == 2:
                book.export(input("Введите имя файла для выгрузки: "), type='csv')
            else:
                filetype = None
                print("Повторите ввод")
        input("Нажмите Enter для продолжения...")
    elif option == 8:
        print('Выберите тип файла для загрузки:')
        print('JSON - 1')
        print('CSV - 2')
        filetype = None
        while filetype == None:
            filetype = input_int()
            if filetype == 1:
                book.load(input("Введите имя файла для загрузки: "), type='json')
            elif filetype == 2:
                book.load(input("Введите имя файла для загрузки: "), type='csv')
            else:
                filetype = None
                print("Повторите ввод")
        input("Нажмите Enter для продолжения...")
    elif option == 9:
        book.purge()
        input("Нажмите Enter для продолжения...")
    elif option == 0:
        finish = True


finish = False
book = PhoneBook()
while not finish:
    main_menu()


# book.reset()
# book.add({"name": "Иванов Иван Иванович", "phone": "12345"})
# book.add({"name": "Петров Петр Петрович", "phone": "123456"})
# book.add({"name": "Сидоров Сидор Сидорович", "phone": "1234567"})
# book.add({"name": "Иванопуло Сидор Магомедович", "phone": "1234568"})

# print(book.get(2))
# print(book.get_all())
# # book.print()
# print(book.find("name", "Сидор"))
# print(book.find("name", "сидор"))


# book.export('export.csv', type = 'csv')
