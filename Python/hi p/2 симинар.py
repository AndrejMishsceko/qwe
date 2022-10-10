## Задача 1
##Вывод произвольного числа n Раз 

# from random import  randrange # импорт функции РАНДИН

# n = int(input("Введите произвольное число: "))
# for _ in range(n):
#     print(randrange(-100,100), end=' ')

##Зада №2
## список из n элементоа



# numbers =  input ("Введите натуральное число: ")
# result = []
# for i in range(1, int(numbers)+1):
#     elem= [i, 3*i +1]
#     result.append(elem)
# print(dict(result))


# numbers =  input ("Введите натуральное число: ")
# result = dict()
# for i in range(1, int(numbers)+1):
#     result[i]= 3*i +1
#    print(result)

 ##Сколько раз встречается вторая строка в первой раз (поиск)


# str1 = input("Ввудите первую строку: ")
# str2 = input("Введите вторую строку: ")
# print(f'Вторая строка входит в первую {str1.count(str2)} раз(а).')