import pyautogui 
import time
import keyboard

while keyboard.is_pressed('t') == False:
    try:
        pyautogui.locateOnScreen('sibs.jpg', )
        print ("Vejo o Sibs")
    except pyautogui.ImageNotFoundException:
        print("Não vejo o mais o Sibs")
    time.sleep(0.5)
