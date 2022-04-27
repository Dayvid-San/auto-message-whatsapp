import pyautogui as pg
import time

time.sleep(10)

# escreva um codigo para a data e hora da mensagem

message = open('mensagem.txt', 'i')

for i in message:
    pg.write(i)
    pg.press('Enter')