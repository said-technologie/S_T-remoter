try :
    import pyautogui
except:
    import os
    os.system("pip install pyautogui > install.txt")
    os.system("pip install pillow > install.txt")
    os.system("rm install.txt")

import pyautogui

def secreen():
    screenshot = pyautogui.screenshot()
    screenshot.save("target.png")