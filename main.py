import pyautogui as pg
import time

name = input("Enter a name?")
time.sleep(5)

txt = open('animals.txt','r')

a = name + ' is a'

for i in txt: 
  pg.write(a + ' ' + i)
  pg.press('Enter')
  time.sleep(1)
