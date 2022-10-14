#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in->out 
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
#- 197.45 -> 27
#                                        Решение:

# from unittest import result
# n= input("Введите двузначное писло: ")
# while not n.isdigit():
#     n = input(" Введите положительное число: ")
# n = int(n)
# def digit_sum(n):
#     n_lst = list(str(n))
#     n_sum = 0
#     for i in range(len(n_lst)):
#         n_sum += int(n_lst[i])
#     return n_sum
# print ("Сумма цифр:",n,"=",digit_sum(n),)   



#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#                                        Решение:
# num = input("Введите число: ")
# while not num.isdigit():
#     num = input(" Ввудите положительное число: ")
# num = int(num)
# result = list()
# j=1
# for i in range(num):
#     j=(i+1)*j
#     result.append(j)
# print(result)



#3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример:
#- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#                                        Решение:
# from unittest import result
# def input_int(msg):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print("Введите положительное число: ")
#         else:
#             return result
# def generate_list(n):
#     result = []
#     for i in range(1, n+1):
#         result.append(round((1+1/i)**i))
#     return result
# n = input_int("Введите число: ")
# number_list = generate_list(n)
# print (f"Для n = {n}: {number_list} - {sum(number_list)}")



##4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
##элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
##Реализуйте алгоритм перемешивания списка.
#                                        Решение:

# from datetime import date
# a=str(input("Введите число №1: "))
# b=str(input("Введите число №2: "))
# with open("fale.txt", "w") as data:          
#     data.writelines("Число №1\n") 
#     data.write(a)
#     data.write("\nЧисло №2\n") 
#     data.write(b)

# f=open("fale.txt", "r")
# lst = f.read().splitlines()####         splitlines() - вывод без "\n"  .readlines() - вывод с "\n"
# i=int(lst[1])
# j=int(lst[3])


# print(lst)

# print("Перемноженные цифры 'a' и 'b' =",i*j)
# f.close()



##                                            Задача №5

#                                        Решение:1
# from random import random
# list=[1,2,3,4,5,6,7,8,9]
# print ("dfgdfgdfg")
# m_list = random.sample(list,len(list))
# print(m_list)

#                                        Решение:2
# from random import choice
# m_list = [1,5,6,5,6,5,9,8,8,6,474,6,5,9,8,5]
# new_list=[]
# for i in m_list:
#     new_list.append(m_list.pop(choice(m_list))) ##pop Не работает
# m_list = list(set(m_list))
# print(list(set(m_list)))
