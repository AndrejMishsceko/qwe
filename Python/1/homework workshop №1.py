##1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
##  является ли этот день выходным.
##Пример:
##- 6 -> да
##- 7 -> да
##- 1 -> нет
# #                                                  Решение:


# a = input("введите номер дня недели: ")
# while  a not in ('1','2','3','4','5','6','7'):
#     print("введите положительное число от 1 до 7")
#     a=input("введите номер дня недели: ")
# a=int(a)
# if a < 6 and a > 0:
#     print("НЕ выходной!! РАБОТАЕМ!!")
# elif a == 6 or a == 7:
#     print("УРАА!! Выходной!!")



##2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
## для всех значений предикат.
##                                                  Решение:

# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(not (x or y or z) == (not x and not y and not z))
#                 print(x, y, z)




##3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
## выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
##Пример:
##- x=34; y=-30 -> 4
##- x=2; y=4-> 1
##- x=-34; y=-30 -> 3
##                                      Мое решение:


# x= float(input("Введите координату Х:"))
# y= float(input("Введите координату Y:"))
# if x==0 or y==0:
#     print("По условию точки не должны быть равные НУЛЮ!",int(x), int(y))
# elif x > 0 and y > 0:
#     print("Первая четверть", x, y)
# elif x > 0 and y < 0:
#     print("Вторая четверть", x, y)
# elif x < 0 and y < 0:
#     print("Третья четверть", x, y)
# elif x < 0 and y > 0:
#     print("Четвертая четверть", x, y)


 ##                                      Решение с защитой от дурака


# x = input("Введите координату Х:")



# while type(x) == float or type(x) == int:#            почемуто не работает(
#     print("Низя координаты обозначать ерундой!ТОЛЬКО ЦИФРЫ! Акстись евлампий!!!")
#     x = input("Введите координату X:")

# while x in("0"):
#     print("По условию точка X не должна быть равной НУЛЮ!")
#     x = input("Введите координату X:")

# y=input("Введите координату Y:")

# while type(y) == int or type(y) == float: #Почемуто не работает
#     print("Низя координаты обозначать ерундой!ТОЛЬКО ЦИФРЫ! Акстись евлампий!!!")
#     y = input("Введите координату Y:")

# while y in("0"):
#     print("По условию точка Y не должна быть равной НУЛЮ!")
#     y = input("Введите координату Y:")

# x = float(x)
# y = float(y)
# if x > 0 and y > 0:
#     print("Первая четверть", x, y)
# elif x > 0 and y < 0:
#     print("Вторая четверть", x, y)
# elif x < 0 and y < 0:
#     print("Третья четверть", x, y)
# elif x < 0 and y > 0:
#     print("Четвертая четверть", x, y)

##4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
## точек в этой четверти (x и y).
##                                      Мое решение:

# i = int(input("Введите номер четверти:"))
# if i==1:
#     print("Х от нуля до + бесконечности, У от нуля до + бесконечности")
# elif i==2:
#     print("Х от нуля до + бесконечности, У от нуля до - бесконечности")
# elif i==3:
#     print("Х от нуля до - бесконечности, У от нуля до - бесконечности")
# elif i==4:
#     print("Х от нуля до - бесконечности, У от нуля до + бесконечности")
# else:
#     print("Введи число от 1 до 4")


##                                       Решение с защитой от дурака:
# i = input("Введи номер четверти: ")
# while  i not in ('1','2','3','4'):
#     print("Введи число от 1 до 4: ")
#     i=input("введите номер четверти: ")
# i=int(i)
# if i==1:
#     print("Х от нуля до + бесконечности, У от нуля до + бесконечности")
# elif i==2:
#     print("Х от нуля до + бесконечности, У от нуля до - бесконечности")
# elif i==3:
#     print("Х от нуля до - бесконечности, У от нуля до - бесконечности")
# elif i==4:
#     print("Х от нуля до - бесконечности, У от нуля до + бесконечности")

##5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними 
## в 2D пространстве.
##Пример:
##- A (3,6); B (2,1) -> 5,09
##- A (7,-5); B (1,-1) -> 7,21


##                                      Pешение:
# import math

# x = int(input("Введите координату Х первой точки: "))
# y = int(input("Введите координату У первой точки: "))
# x1 = int(input("Введите координату Х второй точки: "))
# y1 = int(input("Введите координату У второй точки: "))

# num =int(((x1-x)**2+(y1-y)**2))
# sqrt = math.sqrt(num)
# print("Растояние в 2д пространстве между точками   " + str(sqrt))


                          