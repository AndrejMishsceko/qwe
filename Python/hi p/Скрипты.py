#                                                         ##Проверка
# from unittest import result


# def input_int(msg):
#     while True:
#         try:
#             result = int(input(msg))
#         except ValueError:
#             print("Повторите ввод: ")
#         else:
#             return result

#                                                     ##Печать списка 
# captains = ['Janeway', 'Picard', 'Sisko']
 
# for captain in captains:
#     print(captain)


#                                                     ##Разворот строки
# m_list = [1,3,5,6,8,9,71,12]
# print(m_list[::-1])
# #                                                   ##Разворот текста                                                       
# m_list = "Жопо - руко - ног"
# print(m_list[::-1]) ##      гон - окур - опоЖ



##                                                 ## Удаление "," из строчки 
# string = "3,2.2665"
# number = float(string.replace(",",""))
# print(number)
##                                                 ## Удаление "G" из строчки 
# string = "sdGsagzlkdfjgkl;"
# number = str(string.replace("G",""))
# print(number)

##                                                 Вывод количества индексов массива
# import array as arr
# num = arr.array("i",[11,22,33,44])
# print(len(num))



##                                                  Изменение элемента массива

# import array as arr
# num = arr.array("i",[11,22,33,44])
# num[0]=66
# print(num)

##                                                      Вычисление факториала
# import math
# n=int(input("Введите число для вычисления факториала: "))
# print("фАКТОРИАЛ ЧИСЛА", n, math.factorial(n))



####                                        ФУНКЦИИ


# def new_string(symbol,count):
#     return symbol*count

# print(new_string("!",5)) ##!!!!! получим 5 восклицательных знаков


# def new_string(symbol,count=5):
#     return symbol*count

# print(new_string(5,5)) ##получим 25 перемножим каун и 5



###                                 Работа со строками 

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res+=item
#     return res
# print(concatenatio("a","s","d","w")) ##asdw
# print(concatenatio("a","s","1","2"))  ##as12

###                                 Работа со С ЧИСЛАМИ 

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res+=item
#     return res
# print(concatenatio(1,2,3,4,5,6,8,)) ##Получаем СУММУ чисел


##                                  Рекурсия


# def fib(n):
#     if n in [1,2]: ## Логика выхода из рекурсии
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list=[]
# for e in range(1,10): ##первые 10 чисел фебоначи
#     list.append(fib(e))
# print(list) ## [1, 1, 2, 3, 5, 8, 13, 21, 34]


# ####                            Кортежи - не изменяемый список
# a = (3, 5) ##кортеж из 2х чисел
# print(a)
# print(a[-1])
#             ##Кортеж из одного элемента
# a=(3,)
# a[0]=5 ####Присваивоние делать низяя!

####                                Перебор кортежа 
# a = ("sdf","aeafdfwa","afrweaf","efaef")
# for item in a:
#     print(item)##Выводит по строчно все элементы кортежа

# a = ("sdf","aeafdfwa","afrweaf","efaef")
# for item in a:
#     print(item[1])##Выводи вторуй индекс каждого кортежа


####                                        Словари


# dictionary = {}  ####Создание пустого словаря

#      #### \ - указывается для того чтоб словарь можно было не писать в одну строку
# dictionary = \
#     {
#         "q": "]",
#         "w": "[",
#         "s": "{",
#         "z": "}"
#     }
# # print(dictionary)### {'q': ']', 'w': '[', 's': '{', 'z': '}'} вывод всех элементов словаря
# # print(dictionary["w"])### [


# for k in dictionary.keys():#####Вывод ключей 
#     print(k)



# for v in dictionary.values():#######Вывод значений
#     print(v)


####                                            Множества



# colors= {"red","green","blue"}
# print(colors) ####{'red', 'blue', 'green'}
# colors.add("red")####Добавление во множество имеющегося элемента (добовление элемента не произайдет)
# colors.add("grai")
# print(colors) #####{'green', 'red', 'blue', 'grai'}
# # colors.remove("red")###удаление элемента(если его не будет, при удалении будет ошибка)
# print(colors)###{'blue', 'grai', 'green'}
# colors.discard("red") ###удаление элемента
# print(colors)
# colors.clear()###Очистка множества
# print(colors)


# a={1,2,3,4,5,6,7}
# print(a)
# b={2,3,6,4,11,12,13,20}
# print(b)
# c= a.copy()###{1, 2, 3, 4, 5, 6, 7}
# print(c)
# u=a.union(b)###{1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 20}
# print(u)
# i=a.intersection(b)###{2, 3, 4, 6}
# print(i)
# z=a.difference(b)###{1, 5, 7}
# print(z)
# x=b.difference(a)####{20, 11, 12, 13}
# print(x)

# q=a\
#     .union(b) \
#     .difference(a.intersection(b))#####{1, 5, 7, 11, 12, 13, 20}
# print(q)


# h= frozenset(a)#####Замороженное множество(не изменяемое)


####                        удаление последнего элемента списка POP
# list1= [1,2,3,4,5,6,7]
# print(len(list1))####печать последнего элемента списка
# print(list1.insert(3,11))####добовление элемента 11 в указанный индес
# print(list1.pop())###удаление последнего элемента списка(указать индекс элемента для удаления)
# print(list1)


##########                             Поиск четных и не четных элементов списка и их суммирование

# list_1=[1,1,1,2,1,2,5,]
# summ = 0
# for i in range(1, len(list_1), 2):
#     if i % 2 == 1:
#         summ += list_1[i]       
# print(f"{list_1} -> сумма элементов на нечётных позициях: {summ}")
# for i in range(1, len(list_1), 1):
#     if i % 2 == 1:
#         summ += list_1[i]       
# print(f"{list_1} -> сумма элементов на чётных позициях: {summ}")


#####                               числа фебоначи
# x = y = 1
# n = int(input("Введи число: "))
# for i in range(2, n):
#     x, y = y, x + y
#     # print(y, end=';')
#     print(y)


# Комплексные числа
# сложение : 4 + 4i + 3 + 5i = 7 + 9i
# разница 5 + 4i - (7 + 2i) = -2 + 2i
# умножение (4 + 2i) * (3 + 5i) = 12 + 20i + 6i + 10i^2 = 12 + 26i + 10 *(-1) = 12 + 26i - 10 = 2 + 26i