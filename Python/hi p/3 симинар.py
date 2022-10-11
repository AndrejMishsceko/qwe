# from time import time


# m_time = time()
# # m_time%=1
# print(m_time)
# print(int(m_time %1)*100)



## Задайте список. Напишите программу, которая определит, присуцтвует ли в заданном списке строк некое число.

# m_list=["165","4894","652","316","5456"]
# num = input("Введите число: ")
# for i in m_list:
#     if i == num:
#          print(i)
#          print(m_list.index(i))
#          break

# m_list=["165","4894","652","316","5456"]
# num = input("Введите число: ")
# nol= 0
# for i in m_list:
#     if i == num:
#          print(i)
#          print(m_list.index(i, nol))
#          nol = m_list.index(i,nol)+1
#          break

                                                     ##Перебор (поиск элементов в строке)

# m_list=["165","4894","652","316","5456","165","165"]
# num = input("Введите число: ")

# for i, elem in enumerate(m_list):
#     if num in elem:
#          print(elem)
#          print(i)
         

# m_list=["165","4894","652","316","5456","165","165"]
# num = m_list[0]
# n=0
# for i, elem in enumerate(m_list):
#     if num == elem and i!=0:
#         print(elem)
#         print(i)

                                 ## Все значения в списке по нулевому элементу

# m_list=["165","4894","165","652","316","5456","165","165"]
# num = m_list[0]
# for i in range(1,len(m_list)):
#     if num == m_list[i]:
#         print(i)


                                       ##Только второе значение

# m_list=["165","4894","165","652","316","5456","165","165"]
# num = m_list[0]
# print(m_list.index(num,1))






####                                 Работа с файлами    Способ №1


# from datetime import date


# colors= ["1","2","3","4"]
# data=open("file3.txt", "a")## "a"-открытие для добовления данных(Создает файл если его нет) ,
#                             ##"r"- открытие для чтения данных(если нет файла то ошибка),
#                           ## "w"- открытие для записи заднных,"w+"-,"r+"-
# data.writelines(colors)  #Разделителей не будет
# data.write("\ncolors\n123") ##Дописываем с новой строчки
# data.write("\ncolors")        ##
# data.close()                    ##Закрытие файла



####                                        Способ №2




# with open("file3.txt", "a") as data:           ## Закрывать файл не нужно
#     data.write("\ncolors\n123") 
#     data.write("\ncolors")    


# ####                                       Чтение файла



# path = "file3.txt"###  Указание путя к файлу
# data = open(path,"r")###Открытие для чтения файла
# for line in data:### пробигаемся по файлу
#     print(line)### выводим на печать
# data.close()###закрываем файл

# exit() ###





# from datetime import date



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


# # for k in dictionary.keys():#####Вывод ключей 
# #     print(k)



# # for v in dictionary.values():#######Вывод значений
# #     print(v)








# l=dictionary.values()




# data=open("file3.txt", "w")## "a"-открытие для добовления данных(Создает файл если его нет) ,
#                             ##"r"- открытие для чтения данных(если нет файла то ошибка),
#                           ## "w"- открытие для записи заднных,"w+"-,"r+"-
# data.writelines(l)  #Разделителей не будет
# # data.write("\ncloors\n123") ##Дописываем с новой строчки
# # data.write("\ncolors")        ##
# data.close()                    ##Закрытие файла


