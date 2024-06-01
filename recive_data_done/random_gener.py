import random as r
import time




while True:
    text = 'start\n'
    for i in range(190):
        text +=f"{str(r.randint(1000,9999))}\n"

    with open('D:\BOT.ini', 'w') as bot:
        bot.writelines(text)

    time.sleep(5)