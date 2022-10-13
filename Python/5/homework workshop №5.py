# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
##                                                Решение №1

# import random
# # generate random words from syllables
# syllables = ["ма", "за", "ба", "ка", "ша", "бв"]
# print(random.sample(syllables,2))
# text = list(map(lambda x: "".join(random.sample(syllables,3)), range(random.randint(12,15))))
# print(f' TEXT : {" ".join(text)}')
# print(*text)
# # search for syllable "абв" and delete it with whole word
# parsed_text = list(x for x in text if "абв" not in x)
# print(f'PARSED: {" ".join(parsed_text)}')


##                                                Решение №2

# my_text = 'Скажика дядя ведь не даромабв Москва спалеабвнная пажаром французам отдана'
# print(my_text)

# my_list = my_text.split()
# print(my_list)

# for item in  my_list:
#     if 'абв' in item:
#         my_list.remove(item)

# print(my_list)




# 2. Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from os
# from random import randint

# MAX_COUNT = 2021
# MAX_STEP = 28

# def try_castinput (message, type):
#     result = str()
   
#     try:
#         result = type(input(message))
#     except:
#         result = try_castinput(message, type)

#     return result

# def input_palyer(message):
#     return try_castinput(message, int)
# def input_palyer1(name, count = 0):
#     if name:
#         return "player1"
#     else:
#         return input_palyer('Input player1 count:')
# def input_palyer2(name, count = 0):
#     if name:
#         return "player2"
#     else:
#         return input_palyer('Input player2 count:')
# def input_bot(name, count = 0):    
#     if name:
#         return "bot"
#     else:
#         result = randint(1, MAX_STEP)
#         print('Input bot count:', result)
#         return result
# def input_smartbot(name, count = 0):    
#     if name:
#         return "smartbot"
#     else:
#         result = MAX_COUNT % (MAX_STEP + 1)

#         if count != 0: 
#             result = (MAX_STEP + 1) - count

#         print('Input bot count:', result)

#         return result
# def input_count(play, count):
#     result = 0
#     while not 0 < result < MAX_STEP + 1:
#         result = play(False, count)               
#     return result

# def play(player1, player2):
#     if randint(1, 2) % 2 == 0 or player2(True) == 'smartbot':
#         player1, player2 = player2, player1
    
#     play_sum, prev_sum, idx = 0, 0, 0
#     while play_sum != MAX_COUNT:          
#         print('rest:', MAX_COUNT - play_sum)            
        
#         if idx % 2 == 0:
#             player = player1
#         else: 
#             player = player2
        
#         count = MAX_COUNT + 1
#         while MAX_COUNT - (play_sum + count) < 0:
#             count = input_count(player, play_sum - prev_sum)
        
#         if player(True) not in ('bot', 'smartbot'):
#             system('cls')

#         prev_sum = play_sum
#         play_sum += count
#         idx += 1               

#     print('Winner:', player(True))        

# player_2 = None
# while player_2 not in (1, 2, 3):
#     system('cls')
#     player_2 = try_castinput('input second player(player=1, bot=2 or smartbot=3):', int)

# if  player_2 == 1:
#     play(input_palyer1, input_palyer2)    
# elif player_2 == 2:
#     play(input_palyer1, input_bot)    
# else:
#     play(input_palyer1, input_smartbot) 


###############                             Решение №2

# import random
# # Function checks man to take rules quantity max and min candies
# def man_quantity(min, max):
#     candy = int(input("How many candies you takes?: "))
#     while candy > max or candy < min: 
#         print ("You could take more than 0 and no more than 28 candies!")
#         candy = int(input("How many candies you takes?: "))
#     return candy
# # Function bot take random candies
# def bot_quantity(min, max):
#     candy = random.randint(min, max)
#     print(f"{bot}, takes {candy} candies")
#     return candy
# # Print rules of the game
# text = "On the desk is 2021 candies.\n\
# 2 players make move one by one.\n\
# Who is first player decides the lot.\n\
# With on movie player could take no more than 28 candies\n\
# Winner is player with last move.\n\
# How many candies must take first player to win?"
# print(text)
# # Games VARS, could be changed
# candies = 221
# max = 28
# min = 1
# bot = "Bot"
# ##############################
# man = input("Enter your name: ")
# # First player random choice
# lot = random.choice([man, bot])
# if lot == bot:
#     print(f'First player is {lot}')
# else:
#     print(f"{man}, you're first player")
# # Game core
# while candies > 1:
#     if lot == bot:
#         candies -= bot_quantity(min, max)
#         if candies < 0:
#             break
#         print(f'{candies} candies left')
#         lot = man
#     else:
#         candies -= man_quantity(min, max)
#         if candies < 0:
#             break
#         print(f'{candies} candies left')
#         lot = bot

# # Who is looser :))
# print(f"{lot}, is lost, {candies} candies!")

###############                             Решение №3


# from random import randint, random

# n = 2021
# m = 28

# def my_game(who, how_many, part):
#     game_count = 1
#     if who == 0:
#         right_move = how_many % (part+1)
#         how_many = how_many - right_move
#         print(f'ХОД({game_count}) Bot: я возьму {right_move} конфет')
#         print(f'Остаток конфет: {how_many}')
#         game_count += 1
#         while how_many > 0:
#             while True and how_many>0:
#                 move_player  = int(input(f'ХОД({game_count}) {player}, введите сколько конфет вы хотите взять: ')) 
#                 if move_player > part:
#                     print(f'{player}, количество конфет должно быть меньше {part}')
#                     break
#                 move_bot = part+1-move_player
#                 how_many = how_many - move_player
#                 print(f'Остаток конфет: {how_many}')
#                 game_count += 1
#                 print(f'ХОД({game_count}) Bot: а я возьму {move_bot}')
#                 how_many = how_many - move_bot                
#                 print(f'Остаток конфет: {how_many}')
#         print('Bot: я сделал последний ход и победил! Не переживай, повезет в другой раз!')
#     else:
#         while how_many >0:
#             while True and how_many>0:
#                 move_player  = int(input(f'ХОД({game_count}) {player} введите сколько конфет вы хотите взять: ')) 
#                 if move_player > part:
#                     print(f'{player}, количество конфет должно быть меньше {part}')
#                     break
#                 how_many = how_many - move_player
#                 print(f'Остаток конфет: {how_many}')
#                 if how_many == 0: 
#                     print(f'{player}, ты победил, конфеты твои!!!')
#                     game_count += 1    
#                 else:
#                     if 0 < how_many <= part:
#                         move_bot = how_many
#                     else:
#                         move_bot = randint(1, 28)
#                     print(f'ХОД({game_count}) Bot: а я возьму {move_bot}')
#                     how_many = how_many - move_bot
#                     print(f'Остаток конфет: {how_many}')
#                     if how_many == 0: 
#                         print('Bot: я сделал последний ход и победил! Не переживай, повезет в другой раз!')
#                     game_count += 1

# user_answer = input('Хотите сыграть в игру? "да"/"нет"?: ')
# if user_answer == 'да':
#     player = input('Введите свое имя: ')
#     print('Хорошо! Поехали! А вот и условие. \n На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
#     my_cho = int(randint(0,1))
#     if my_cho == 1:
#         print(f'{player}, Ты ходишь первый!')
#     else:
#         print('Я хожу первый!')
#         print('Поехали!')
#     my_game(my_cho, n, m)
# else:
#     print('Ну и не надо =(')

###############                             Решение №4

# import os
# from random import randint
# os.system('cls')

# konfety = 2021  # Указать сколько конфет на кону

# def type_game(): # функция выбора типа игры, два человека или с ботом
#     is_OK = True
#     while is_OK:
#         try:
#             select = int(input('Выберете вариант игры (2 - игра в двоем, любое другое число - игра с ботом) - '))
#             if select == 2:
#                 user1 = input('Игорок 1, представьтесь - ')
#                 user2 = input('Игорок 2, представьтесь - ')
#                 gamer = user1
#                 is_OK = False
#             else:
#                 user1 = input('Игорок 1, представьтесь - ')
#                 user2 = 'bot'
#                 gamer = user1
#                 is_OK = False
#         except ValueError:
#             print()
#     return user1, user2, gamer

# def take_hod(player): # фукнция хода игрока 
#     global konfety
#     while True:
#         try:
#             hod = int(input('Сколько взять конфет (1-28),  ' + player + ' ? '))
#             if hod >= 1 and hod <= 28 and hod <= konfety:
#                 konfety -= hod
#                 os.system('cls')
#                 break
#             else:
#                 print('Введите от 1 до 28 для хода')
#                 continue
#         except ValueError:
#             print()
#         break

# def check_win(): # функция проверка на выигрыш
#     if konfety == 0:
#         return True
#     else:
#         return False

# def bot(): # функция хода бота
#     global konfety
#     while True:
#         hod = randint(1, 28)
#         if konfety <= 28:
#             hod = konfety
#             konfety -= hod
#             print('Бот взял', hod, 'конфет')
#             break
#         if hod <= konfety:
#             konfety -= hod
#             print('Бот взял', hod, 'конфет')
#             break
#         else:
#             continue

# def game(): # функция самой игры и смены ходов
#     a = 0 # счетчик ходов
#     b = 2 # константа для проверки выиграша
#     user1, user2, gamer = type_game()
#     while True:
#         print('Осталось', konfety, 'конфет')
#         if a % 2 == 0: # если ход четный, ходит первый игрок
#             take_hod(user1)
#             gamer = user1
#         elif user2 in 'bot':
#             bot()
#             gamer = 'Бот'
#         else:
#             take_hod(user2)
#             gamer = user2
#         if b > konfety // 28: # проверка выигрыша начинаеться только если осталось чуть более двух ходов
#             win = check_win()
#             if win:
#                 os.system('cls')
#                 print(gamer, 'Выиграл!!!')
#                 break
#         a += 1 # счетчик ходов
#         print(konfety//28)

# game()


###############                             Решение №4


# from random import randint
# import os
# os.system('cls')


# def checking_input(name):
#     n = (
#         input(f'\n{name}, введите количество конфет, которое возьмете от 1 до 28: '))
#     while not n.isdigit():
#         n = (
#             input(f'{name}, введите корректное количество конфет: '))
#     n = int(n)
#     os.system('cls')
#     return (n)


# def input_dat(name):
#     x = checking_input(name)
#     while x < 1 or x > 28:
#         x = checking_input(name)
#     return x


# def input_bot(name):
#     if counter1 == 0:
#         k = randint(1, 28)
#     else:
#         k = 29 - includ
#     return k


# def motion_print(name, k, counter, value):
#     print(
#         f'Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.')


# print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
# input('\nДля начала игры нажмите "Ввод"')
# os.system('cls')
# player1 = input('Введите имя первого игрока: ')
# player2 = input(
#     '\nВведите имя второго игрока, или введите Бот для игры с ботом: ')

# if player2 == 'Бот':
#     player3 = player2
# value = int(input('Введите количество конфет на столе(2021): '))
# counter1 = 0
# counter2 = 0
# counter3 = 0
# includ = 0
# print('\nКоличество конфет на столе:', value)
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f'Первый ходит {player1}')
# elif flag and player2 == 'Бот':
#     print(f'Первый ходит {player3}')
# else:
#     print(f'Первый ходит {player2}')

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         includ = k
#         flag = False
#         motion_print(player1, k, counter1, value)
#     elif player2 == 'Бот':
#         k = input_bot(player3)
#         counter3 += k
#         value -= k
#         flag = True
#         motion_print(player3, k, counter3, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         motion_print(player2, k, counter2, value)

# if flag:
#     print(f'Выиграл {player1}')
# else:
#     print(f'Выиграл {player2}')






# 3. Создайте программу для игры в ""Крестики-нолики"".


# import os
# os.system('cls')

# pole = list(range(1, 10))

# win_komb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# def draw_pole(): # функция отрисовки игрового поля
#     print('-------------')
#     for i in range(3):
#         print('|', pole[0 + i*3], '|',
#               pole[1 + i*3], '|', pole[2 + i*3], '|')
#     print('-------------')

# def take_hod(player): # фукнция хода игрока
#     while True:
#         hod = input('Куда поставить ' + player + ' ? ')
#         if  hod not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print('Введите вереый номер клеточки для хода')
#             continue
#         hod = int(hod)
#         if str(pole[hod-1]) in 'XO':
#             print('Клетка занята, выберите другую')
#             continue
#         pole[hod-1] = player
#         break

# def check_win(): # функция проверка на выигрыш
#     for elem in win_komb:
#         if pole[elem[0]] == pole[elem[1]] == pole[elem[2]]:
#             return pole[elem[0]]
#     else:
#         return False

# def game(): # функция самой игры и смены ходов
#     a = 0
#     while True:
#         os.system('cls')
#         draw_pole()
#         if a % 2 == 0: 
#             take_hod('X')
#         else:
#             take_hod('O')
#         if a > 3:
#             win = check_win()
#             if win:
#                 os.system('cls')
#                 draw_pole()
#                 print(win, 'Выиграл!!!')
#                 break
#         a += 1
#         if a > 8:
#             os.system('cls')
#             draw_pole()
#             print('Ничья!!')
#             break
# game()


###############                             Решение №2


# empty_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# def print_field(field):
#     print("┌───┬───┬───┐")
#     print("│ "+" │ ".join(field[0])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[1])+" │")
#     print("├───┼───┼───┤")
#     print("│ "+" │ ".join(field[2])+" │")
#     print("└───┴───┴───┘")


# def make_move(field, move, symbol):
#     result = field.copy()
#     move = move.split()
#     [x, y] = list(map(int, move))
#     if (3 > x >= 0) and (3 > y >= 0) and result[y][x] == " ":
#         result[y][x] = symbol
#     else:
#         new_attempt = input("Неправильный ход, повторите ввод: ")
#         result = make_move(field, new_attempt, symbol)
#     return result


# def check_win(field):
#     # проверка ряда
#     for row in field:
#         if row[0] == "X" and row[1] == "X" and row[2] == "X":
#             return "X"
#         if row[0] == "0" and row[1] == "0" and row[2] == "0":
#             return "0"
#     # проверка колонки
#     for col in range(3):
#         if field[0][col] == "X" and field[1][col] == "X" and field[2][col] == "X":
#             return "X"
#         if field[0][col] == "0" and field[1][col] == "0" and field[2][col] == "0":
#             return "0"
#     # проверка диагонали
#     if field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
#         return "X"
#     if field[0][2] == "X" and field[1][1] == "X" and field[2][0] == "X":
#         return "X"
#     if field[0][0] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     if field[0][2] == "0" and field[1][1] == "0" and field[2][0] == "0":
#         return "0"
#     return None


# field = empty_field
# moves_count = 0
# is_X_move = True
# print("Добро пожаловать в игру X-0. В свой ход вводите координаты, разделенные пробелом.")
# while check_win(field) == None and moves_count < 9:
#     current_player = "X" if is_X_move else "0"
#     field = make_move(field, input(
#         f"Ход игрока {current_player}: "), current_player)
#     print_field(field)
#     is_X_move = not is_X_move
#     moves_count += 1
# print("Игра окончена")
# result = check_win(field)
# if result == None:
#     print("Ничья")
# else:
#     print(f"Победитель: игрок {result}")


###############                             Решение №3

# def field(moves):
#     y0 = f"    X1    X2   X3  "
#     y1 = f"Y1  {moves['y1']['x1']}  |  {moves['y1']['x2']}  | {moves['y1']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y2 = f"Y2  {moves['y2']['x1']}  |  {moves['y2']['x2']}  | {moves['y2']['x3']}  "
#     y1_1 = "  -----+-----+-----"
#     y3 = f"Y3  {moves['y3']['x1']}  |  {moves['y3']['x2']}  | {moves['y3']['x3']}  "
#     print(y0)
#     print(y1)
#     print(y1_1)
#     print(y2)
#     print(y1_1)
#     print(y3)

# def check(move, moves):
#     if len(move) == 4:
#         if move[0].lower() == 'y' and move[2].lower() == 'x':
#             if move[1] in '123' and move[-1] in '123':
#                 if moves[move[:2]][move[-2:]] == ' ':
#                     return True
#                 else:
#                     print('Данная клетка уже занята.')
#             else:
#                 print('Введены недопустимые значения координат.')
#         else:
#             print('Вы ввели не допустимые оси координат')
#     else:
#         print('Введено недопустимое количество символов.')
#     print('Попробуйте ещё раз!')
#     return False

# def wins(moves):
#     if ((moves['y1']['x1'] == moves['y1']['x2'] == moves['y1']['x3']
#             or moves['y1']['x1'] == moves['y2']['x1'] == moves['y3']['x1']
#             or moves['y1']['x1'] == moves['y2']['x2'] == moves['y3']['x3'])
#             and moves['y1']['x1'] != ' '):
#         return moves['y1']['x1']
#     elif ((moves['y2']['x1'] == moves['y2']['x2'] == moves['y2']['x3']
#            or moves['y1']['x2'] == moves['y2']['x2'] == moves['y3']['x2']
#            or moves['y1']['x3'] == moves['y2']['x2'] == moves['y3']['x1'])
#           and moves['y2']['x2'] != ' '):
#         return moves['y2']['x2']
#     elif ((moves['y3']['x1'] == moves['y3']['x2'] == moves['y3']['x3']
#            or moves['y1']['x3'] == moves['y2']['x3'] == moves['y3']['x3'])
#           and moves['y3']['x3'] != ' '):
#         return moves['y3']['x3']
#     return False


# def move(symbol, moves, player):
#     print('Текущий ход y{}x{}'.format(player[1], player[-1]))
#     if player[1] == '1':
#         if player[-1] == '1':
#             moves['y1']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y1']['x2'] = symbol
#         else:
#             moves['y1']['x3'] = symbol
#     elif player[1] == '2':
#         if player[-1] == '1':
#             moves['y2']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y2']['x2'] = symbol
#         else:
#             moves['y2']['x3'] = symbol
#     else:
#         if player[-1] == '1':
#             moves['y3']['x1'] = symbol
#         elif player[-1] == '2':
#             moves['y3']['x2'] = symbol
#         else:
#             moves['y3']['x3'] = symbol
#     return moves


# moves_out = {
#     'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
#     'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
# }

# field(moves_out)

# number_players = int(input('Введите количество игроков (1/2): '))
# count_move = 0

# if number_players == 2:
#     win = False
#     while not win and count_move < 9:
#         count_move += 1
#         player_out = input('Введите координаты хода(пример - y2x3): ')
#         while not check(player_out, moves_out):
#             player_out = input('Введите координаты хода(пример - y2x3): ')
#         if count_move % 2:
#             symbol_out = 'X'
#         else:
#             symbol_out = 'O'
#         moves_out = move(symbol_out, moves_out, player_out)

#         field(moves_out)
#         win = wins(moves_out)
#     if count_move == 9:
#         print('Ничья!')
#     else:
#         print(f'На {count_move} ходу победили "{win}"')



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.



# import os
# os.system('cls')

# def encode_file(my_text):  # функция кодировая текста
#     str_code = ''
#     count = 1       
#     for i in range(len(my_text)):
#         if i < len(my_text)-1:
#             if my_text[i] == my_text[i + 1]:
#                 count += 1
#             else:
#                 str_code += str(count) + my_text[i]
#                 count = 1
#         else:
#             str_code += str(count) + my_text[i]
#     return str_code

# def decode_file(str_code): # функция раскодирования текста
#     count = ''
#     my_text = ''
#     for i in str_code:
#         if i.isdigit():
#             count += i
#         else:
#             my_text += i * int(count)
#             count = ''
#     return my_text


# with open('decode.txt', 'r') as data: # считали исходный текст
#     my_text = data.read()

# print('Исходный текст', my_text)
# code_text = encode_file(my_text) # закодировали исходный текст
# print('Текст после кодирования', code_text)

# with open('encode.txt', 'w') as data: # записали закодированный текст
#     data.write(code_text)
    
# with open('encode.txt', 'r') as data: # считали закодированый текст
#     str_code = data.read()

# my_text = decode_file(str_code) # раскодировали текст
# print('Раскодированный текст', my_text)


###############                             Решение №2


# def encoding(text):
#     code_text = ""
#     count = 0
#     repetitions = 1
#     while count < len(text):
#         try:
#             if text[count] == text[count+1]:
#                 repetitions += 1
#             elif repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#                 repetitions = 1
#         except IndexError:
#             if repetitions == 1:
#                 code_text += text[count]
#             elif repetitions > 1:
#                 code_text += str(repetitions) + text[count]
#         count += 1
#     return code_text
# # Function to decode given cipher
# def decoding(cipher):
#     decoded_text = ""
#     count = 0
#     repetitions = 0
#     while count < len(cipher):
#         if str(cipher[count]).isdigit():
#             repetitions = int(cipher[count])
#         elif repetitions > 0:
#             for x in range(repetitions):
#                 decoded_text += cipher[count]
#                 repetitions = 0
#         elif repetitions == 0:
#             decoded_text += cipher[count]
#         count +=1
#     return decoded_text
# # Text input  
# text = input("Enter a text: ")
# # Decides encode or decode
# numbers_in_text = 0
# for num in text:
#     if num.isdigit():
#         numbers_in_text += 1
# # If any digits exists it mean coded text, decoding
# if numbers_in_text > 0:
#     print(f"Decoding: {decoding(text)}")
# # If no digits exists it mean pure text, encoding
# else:
#     print(f"Encoding: {encoding(text)}")

###########                                     Кодировка и раскодировка из файлов


# with open('decode.txt', 'r') as data: # считали исходный текст
#     my_text = data.read()
# print('Исходный текст', my_text)
# code_text = encode_file(my_text) # закодировали исходный текст
# print('Текст после кодирования', code_text)
# with open('encode.txt', 'w') as data: # записали закодированный текст
#     data.write(code_text)
# with open('encode.txt', 'r') as data: # считали закодированый текст
#     str_code = data.read()
# my_text = decode_file(str_code) # раскодировали текст
# print('Раскодированный текст', my_text)
