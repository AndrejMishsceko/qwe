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



                                                   ## Изменение элемента массива

# import array as arr
# num = arr.array("i",[11,22,33,44])
# num[0]=66
# print(num)

##                                                      Вычисление факториала
# import math
# n=int(input("Введите число для вычисления факториала: "))
# print("фАКТОРИАЛ ЧИСЛА", n, math.factorial(n))


