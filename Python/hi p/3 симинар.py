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