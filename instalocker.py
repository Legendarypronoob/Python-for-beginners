import pyautogui


def main():
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


if __name__ == "__main__":
    while True:
        main()


