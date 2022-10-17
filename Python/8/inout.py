def enter():
    return input()
def out(book):
    print(book)
    

def write_book(book):
    var_write = int(input('В каком формате записывем? \n 1. в .txt \n 2. в .csv \n'))
    if var_write == 1:
        with open ('adrbk.txt', 'a') as data:
            book = str(book)
            data.write(book)
            data.write('\n')
    else:
        with open ('adrbk.csv', 'a') as data:
            book = str(book)
            data.write(book)
            data.write('\n')
            