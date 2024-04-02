from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#X:  186 Y:  350 RGB: (156, 162, 231)
#X:  272 Y:  691 RGB: (155, 162, 230
#X:  355 Y:  690 RGB: (164, 169, 232)
#X:  432 Y:  685 RGB: (253,  18,   1)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time;sleep(0.01) #pause
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(193, 350)[0] == 0:
        click(193, 350)
    if pyautogui.pixel(283, 350)[0] == 0:
        click(283, 350)
    if pyautogui.pixel(355, 350)[0] == 0:
        click(355, 350)
    if pyautogui.pixel(432, 350)[0] == 0:
        click(432, 350)
