# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:* 
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
##                                          решение  которое можно взломать. Использовать нежелательно!!!
# calc= input("Введите выражение: ")
# m_list = eval(calc)
# print(m_list)

##                                          решение 
# my_text = '1-2*3*4*2+8/4+9-3+7'
# my_list = list(my_text)
# print(my_list)



# i = 1

# while '*' in my_list or '/' in my_list:
#     if my_list[i] == '*':
#         my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#         del my_list[i+1]
#         del my_list[i]
#     elif my_list[i] == '/':
#         my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#         del my_list[i+1]
#         del my_list[i]
#     else: i += 1    

# i = 1

# while '+' in my_list or '-' in my_list:
#     if my_list[i] == '+':
#         my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#         del my_list[i+1]
#         del my_list[i]
#     elif my_list[i] == '-':
#         my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#         del my_list[i+1]
#         del my_list[i]
#     else: i += 1   
# print(my_list)






    # - Добавьте возможность использования скобок, меняющих приоритет операций.
    #     *Пример:* 
    #     1+2*3 => 7; 
    #     (1+2)*3 => 9;

# my_text = '1-2*3*4*(2+8*2)/4+9-3+7'
# my_list_out = list(my_text)
# print(my_list_out)

# def calc(my_list):
#     i = 1

#     while '*' in my_list or '/' in my_list:
#         if my_list[i] == '*':
#             my_list[i-1] = int(my_list[i-1]) * int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '/':
#             my_list[i-1] = int(my_list[i-1]) / int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else: i += 1    

#     i = 1

#     while '+' in my_list or '-' in my_list:
#         if my_list[i] == '+':
#             my_list[i-1] = int(my_list[i-1]) + int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         elif my_list[i] == '-':
#             my_list[i-1] = int(my_list[i-1]) - int(my_list[i+1])
#             del my_list[i+1]
#             del my_list[i]
#         else: i += 1
#     return my_list


# while '(' in my_list_out:
#     bracket_left = my_list_out.index('(')
#     bracket_right = my_list_out.index(')')
#     my_list_out = my_list_out[:bracket_left] + calc(my_list_out[bracket_left + 1 : bracket_right]) + my_list_out[bracket_right + 1 :]

# print(my_text + '=>' + str(calc(my_list_out)[0]))

####                                  

# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# new_list = []
# for i in range(0,len(my_list)):
#     if my_list.count(my_list[i]) == 1:
#         new_list.append(my_list[i])
# print(new_list)

####                                    Второе решение со вводом через пробелы



enum_number = list(map(int, input("Введите натуральные числа через пробел :").split()))

enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

print(enum_number, '->', enum_unique)