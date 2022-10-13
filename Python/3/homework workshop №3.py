# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# ###                                     Решение:1
# list_1=[1,2,3,4,5,6,7,8]
# y = 0
# for i in range(1, len(list_1), 2):
#     if i % 2 == 1:
#         y += list_1[i]       
# print(f"{list_1} -> сумма элементов на чётных позициях: {y}")

# ###                                     Решение:2
# list_1 = [1,2,3,4,5,6,7,8]
# list_ch = sum(list_1[::2])
# list_nch = sum(list_1[1::2])
# print(f"{list_1} -> сумма элементов на нечётных позициях: {list_ch}")
# print(f"{list_1} -> сумма элементов на чётных позициях: {list_nch}")


#2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# ###                                     Решение:
# list_1 = [2, 3, 5, 6]
# list = []
# for i in range((len(list_1)+1)//2):
#     list.append(list_1[i]*list_1[len(list_1)-1-i])
# print(list)



# 3. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# ###                                         Решение1: 

# list_1 = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in list_1:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)

# ###                                         Решение2: 

# list_1 = [1.1, 1.2, 3.1, 5, 10.01]
# List_n = [round( i  % 1, 2) for i in list_1 if i % 1 != 0]
# print(f'{list_1} => {max(List_n)-min(List_n)}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

#####                                    Решение: 1

# x = int(input("Введи число: "))
# print(bin(x))

########                                Решение 2
# x = int(input("Введи число: ")) 
# y = ''
# while x > 0:
#     y = str(x % 2) + y
#     x = x // 2
# print( f"двоичное представление числа = {y}")





#5.  Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# x = y = 1
# n = int(input("Введи число: "))
# for i in range(2, n):
#     x, y = y, x + y
#     # print(y, end=';')
#     print(y)####Просто вывод числа фибоначи



# ###############################             Решение


# def fibonacci(n):
#     first, second = 0, 1
#     fibonacci_num = 0
#     for i in range(n):
#         fibonacci_num = first + second
#         second = first
#         first = fibonacci_num
#     return fibonacci_num

# def negative_fibonacci(n):
#     if n ==1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1-num2
#         return num2

# set_number = (input("Ввудите число: "))
# while not set_number.isdigit():
#     set_number = (input("Введите число "))
# set_number = int(set_number)
# list = [0]
# for i in range(1,set_number +1):
#     list.append(fibonacci(i))
#     list.insert(0,negative_fibonacci(i))
# print(list)








