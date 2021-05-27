#this is the main of the tools 
#S_T v1.0
#cheking the modules 
from templets.module_cheeke.module import modules_check
'''checking the modules'''
modules_check()
'''checking if user have ben install ngrok'''
#ngrok_check()
'''importing the needing modules'''

import os, sys, time
from templets.banner.banner import *
from templets.function import *
from tips.tip import *
from server_host.session import *
#seting the colors variables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[0m"
#building the user intarface

def S_T():
    os.system("clear")
    print(f"{c}  [{g}   OK   {c}] {g} all the module are founds")
    os.system("clear")
    time.sleep(2)
    print(f"{v}  [{g}+{v}]{g}  starting ...{none}")
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    interface_banner()
    tips()
    while True:
        op_intarface = input(f"{r}#{y}S_T-remoter{r}>> {g}")
        if op_intarface == "exit":
            print(f"{v}  [{r}!{v}] {y}exiting...{none}")
            time.sleep(3)
            sys.exit()
        elif op_intarface == "clear":
            os.system("clear")
        elif op_intarface == "help":
            help_menu()
        #checking teh cre_channel options Github
        elif op_intarface == "cre_channel -c Github":
            channel.github_T_L()
        #checking teh cre_channel options Youtube
        elif op_intarface == "cre_channel -c Youtube":
            channel.youtube_T_L()
        #checking the cre_channel options Facebook
        elif op_intarface == "cre_channel -c Facebook":
            channel.facebook_T_L()
        #check the status of the user
        elif op_intarface == "get status":
            status()
        #check for update
        elif op_intarface == "update":
            git_repo()
        #the usage command
        elif op_intarface == "usage get status":
            usage.usage_get_status()
        elif op_intarface == "usage start server":
            usage.usage_start_server()
        elif op_intarface == "usage cre_channel":
            usage.usage_cre_channel()
        #start a server option
        elif op_intarface[0:11] == "start server":
            reverse_shell_exec()
        elif op_intarface[0:] == "exploit-payload":
            payload.Termux(op_intarface)
        else :
            print(f"  {c}[{r}-{c}]{r}  command not found : {y}{op_intarface}")
if __name__ == "__main__":
    S_T()
