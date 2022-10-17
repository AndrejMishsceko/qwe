import adressbook as ab
import inout as io

def start():
    print('Введите имя ')
    value_n = (io.enter())
    print('Введите телефон ')
    value_p = io.enter()
    print('Введите адрес ')
    value_a = io.enter()
    print('Введите статус ')
    value_s = io.enter()
    ab.init(value_n, value_p, value_a, value_s)
    result = ab.add_zip()
    io.out(result)
    io.write_book(result)