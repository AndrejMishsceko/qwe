#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#in->out 
#Пример:
#- 6782 -> 23
#- 0,56 -> 11
#- 197.45 -> 27


# from unittest import result


# n= input("Введите писло: ")

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








siza= int(input("Введите число"))
numb_list= list(range(-siza,siza+1))
path= "file.txt"
date = open(path,"r")
sum=1
for position in date:
    sum*= numb_list[int(position)]
date.close()
print(numb_list)
print(sum)


