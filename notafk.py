import pyautogui
import pyautogui as pag
import random
import time

# for valorant

while True:
    x = random.randint(0, 1366)
    y = random.randint(0, 768)
    pyautogui.click(x, y, 2)
    pyautogui.hotkey("enter")
    pyautogui.typewrite("I am afk I will be back soon. Love ya!")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("space")
    time.sleep(1)
