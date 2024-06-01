import serial
import time



way_for_ini = r'D:\BOT.ini'
com_port = "COM5"


def open_port():
    try:
        s=serial.Serial(com_port, 9600)
        time.sleep(2)
        s.reset_input_buffer()
    except Exception:
        time.sleep(2)
        open_port()
    return s


def write_data(f):
    time.sleep(0.9)
    write = ser.write(f)
    print("---Данные отправлены---")




def list_of_ini(way: str)-> bytearray : 
    '''Функция принимает ini файл и возвращает байтовую строку'''


    with open(way_for_ini,'r') as bot:
        data = bot.readlines()
        data = data[1::]
        data = list(map(lambda x: x[:-1], data))
        for i in range(len(data)):
            index = data[i].find('=') + 1
            data[i] = data[i][index::]
        data = str(data).encode()
    return data


ser = open_port()
while True:
    data_in_ser = list_of_ini(way_for_ini)
    print(data_in_ser)
    if ser:
        pass
    else:
        ser = open_port()
        if ser:
            print(ser)
            print("-----Порт открыт-----")
    write_data(data_in_ser)
    try:
        write_data(data_in_ser)
    except Exception:
        print('Что-то не то')
        continue
