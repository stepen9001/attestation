import serial
from threading import *
import time


#Чтение файла конфигурации
def open_config():
    with open(r'.\\config.ini', 'r', encoding='utf-8') as ini_com:
        port = ini_com.readline().strip()
        way_in_rasch = ini_com.readline().strip()
        time_sleep = int(ini_com.readline().strip())
        arc = ini_com.readline().strip()
        dot_lst = ini_com.readline().strip()
        print("Порт задействован -", port)
        print("Путь к расчетной станции -", way_in_rasch)
        print("Время до перезагрузки программы при отсутствии данных. В секундах -",time_sleep)
        print("Путь к архиву данных, переданных в рассчетку -", arc)
        print("Путь к файлу списка точек для выгрузк -", dot_lst)
        return port, way_in_rasch, time_sleep, arc, dot_lst

#Получение списка точек
def dots_list():
    dots_list = open (dot_lst,'r', encoding='utf-8')
    dots_array_0 = dots_list.readlines()
    dots_list_out = [dots_list.strip() for dots_list in dots_array_0 if dots_list.strip() != '']
    dots_list.close()
    DOTS = dots_list_out
    return DOTS

#Открытие порта
def open_port():
    try:
        s=serial.Serial(port, 9600)
        time.sleep(2)
        s.reset_input_buffer()
    except Exception:
        time.sleep(2)
        open_port()
    return s

#Запись в INI
def write_in_ini(list_data):
    
    '''Записывает точки и значения в INI'''
    
    list_data = list_data[1:-1].split(',')
    arr = []
    z = 0
    for i in DOTS:
        arr.append(i+'='+list_data[z])
        
        z+=1
        
    while True:
        if arr[0].endswith("'0.000'") and arr[5].endswith("'0.000'") and arr[10].endswith("'0.000'"):
            print("НУЛЕВЫЕ ЗНАЧЕНИЯ")
            break
        try:
            ini = open(way_in_rasch, 'w',encoding='utf-8')
            #ini.write('[DOTS]\n')
            for i in arr:
                ini.write(str(i)+'\n')
            print("-----ДАННЫЕ ЗАПИСАНЫ-----\n")
            ini.close()
            break                
        except Exception:
            continue

def write_in_txt(list_data):
    
    '''Записывает точки и значения в txt'''
    txt = open(arc, 'a',encoding='utf-8')
    txt.write(list_data+'\n')
    txt.close()             

def main():
    global ser, output_data, control
#Основной цикл программы
    while True:
        if ser:
            pass
        else:   #Открываем порт
                ser = open_port()
                if ser:
                    print('-----Порт открыт-----')
        try:
            #Читаем данные
            reading = ser.read().decode()
        except Exception:
            ser = ''
            continue
    #Формирование строки
        if reading =='[':
            output_data = ''
            output_data = output_data + reading
            
        elif len(reading) > 0 and reading not in ['[',']']:
            output_data = output_data + reading
            
        elif reading == ']' and output_data.startswith('['):
            output_data = output_data + reading
            print(output_data)
            #Записываем в INI
            if len(output_data.split(',')) == len(DOTS):
                write_in_ini(output_data)
            #write_in_txt(time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())+ ' ' + output_data)
            #Обнуляем массив данных для нового цикла
            control = output_data
            output_data = ''

def two():
    global control
    while True:
        time.sleep(time_sleep/2)
        o_d_1 = control
        time.sleep(time_sleep/2)
        o_d_2 = control
        if o_d_1 == o_d_2:
            print("-----ПЕРЕЗАПУСК-----")
            time.sleep(3)
            exit()


#Объект параллельного порта
ser = ''
#Выходная строка данных
output_data = ''
#Переменная для контроля обновления значений
control = ''
# Выгружаем информацию из файла CONFIG.INI 
port, way_in_rasch, time_sleep, arc, dot_lst = open_config()
#Выгружаем список точек
DOTS = dots_list()

print("Точек всего передается -", len(DOTS))
print(DOTS)
main()
#t_1 = Thread(target = main)
#t_2 = Thread(target = two)


#t_1.daemon = True
#t_1.start()
#t_2.start()

#t_2.join()
