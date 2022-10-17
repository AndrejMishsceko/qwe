import controller

des = int(input('Что будем делать?\n 1. Добавляем в адресную книгу \n 2. Смотрим что есть в адресной книге\n'))
if des == 1:
    controller.start()
else:
    var_read = int(input('Какой формат будем читать? \n 1. .txt \n 2. .csv \n'))
    if var_read == 1:
        data = open('adrbk.txt', 'r')
        for line in data:
            print(line) 
        data.close()
    else: 
        data = open('adrbk.csv', 'r')
        for line in data:
            print(line) 
        data.close()
