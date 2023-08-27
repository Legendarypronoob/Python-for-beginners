import pyautogui
import random
import time
import keyboard

reyna_running = False
afk_running = False


def afk():
    k = random.randint(0, 1366)
    i = random.randint(0, 768)
    pyautogui.click(k, i, 2)
    pyautogui.hotkey("enter")
    pyautogui.typewrite("I am afk I will be back soon. Love ya!")
    pyautogui.hotkey("enter")
    pyautogui.hotkey("space")
    time.sleep(1)


def reyna():
    try:
        reyna_position = pyautogui.locateOnScreen("reyna.png", grayscale=True, confidence=0.5)
        if reyna_position:
            reyna_x, reyna_y = pyautogui.center(reyna_position)
            pyautogui.click(reyna_x, reyna_y)
            print("Clicked on Reyna")

            lockin_position = pyautogui.locateOnScreen("lockin.png", grayscale=True, confidence=0.5)
            if lockin_position:
                lockin_x, lockin_y = pyautogui.center(lockin_position)
                pyautogui.click(lockin_x, lockin_y)
                print("Locked in")
            else:
                print("Lock In button not found")
        else:
            print("Reyna button not found")
    except Exception as e:
        print("An error occurred:", str(e))


def toggle_reyna_state():
    global reyna_running
    reyna_running = not reyna_running
    return reyna_running


def toggle_afk_state():
    global afk_running
    afk_running = not afk_running
    return afk_running


if __name__ == "__main__":
    print("Press '9' to start/stop the Reyna loop")
    keyboard.add_hotkey("9", toggle_reyna_state)

    print("Press '0' to start/stop the AFK loop")
    keyboard.add_hotkey("0", toggle_afk_state)

    while True:
        if reyna_running:
            reyna()
        if afk_running:
            afk()
        time.sleep(0.1)
