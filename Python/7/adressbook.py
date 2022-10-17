name = str
phone = str
adress = str
status = str

def init(n, p, a, s):
    global name
    global phone
    global adress
    global status
    name = n
    phone = p
    adress = a
    status = s

def add_zip():
    # data = open('adrbk.txt', 'a')
    # data.writelines('{name}, {phone}, {adress}, {status} \n')
    # with open ('adrbk.txt', 'a') as data:
    #     data.write('{n}, {p}, {a}, {s} \n')
    return name, phone, adress, status
   