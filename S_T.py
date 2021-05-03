#this is the main of the tools 
#S_T v1.0
#cheking the modules 
from templets.module_cheeke.module import modules_cheke

modules_cheke()
#importing the needing modules

import os, sys, time
from templets.banner.banner import *
from templets.function import *
from colorama import *
#seting the colors variables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"
#building the user intarface

def S_T():
    os.system("clear")
    print(f"{c}  [{g}   OK   {c}] {g} all the module are founds")
    time.sleep(2)
    print(f"{v}  [{g}+{v}]{g}  starting ...{none}")
    time.sleep(2)
    os.system("clear")
    time.sleep(2)
    interface_banner()
    while True:
        op_intarface = input(f"{r}#{y}S_T-remoter{r}>> {g}")
        if op_intarface == "exit":
            print(f"{v}  [{r}!{v}] {y}exiting...")
            time.sleep(3)
            sys.exit()
        elif op_intarface == "clear":
            os.system("clear")
        elif op_intarface == "help":
            help_menu()
        #cheking teh cre_channel options Github
        elif op_intarface == "cre_channel -c Github -o Termux":
            channel.github_T_L()
        elif op_intarface == "cre_channel -c Github -o Linux":
            channel.github_T_L()
        elif op_intarface == "cre_channel -c Github -o Windows":
            channel.github_W_M()
        elif op_intarface == "cre_channel -c Github -o Mac":
            channel.github_W_M()
        #cheking teh cre_channel options Youtube
        elif op_intarface == "cre_channel -c Youtube -o Termux":
            channel.youtube_T_L()
        elif op_intarface == "cre_channel -c Youtube -o Linux":
            channel.youtube_T_L()
        elif op_intarface == "cre_channel -c Youtube -o Windows":
            channel.youtube_W_M()
        elif op_intarface == "cre_channel -c Youtube -o Mac":
            channel.youtube_W_M()
        #cheking teh cre_channel options Facebook
        elif op_intarface == "cre_channel -c Facebook -o Termux":
            channel.facebook_T_L()
        elif op_intarface == "cre_channel -c Facebook -o Linux":
            channel.facebook_T_L()
        elif op_intarface == "cre_channel -c Facebook -o Windows":
            channel.facebook_W_M()
        elif op_intarface == "cre_channel -c Facebook -o Mac":
            channel.facebook_W_M()
        #cheking if the len of intup is 0
        elif len(op_intarface) == 0:
            return op_instarface
        else :
            print(f"  {c}[{r}-{c}]{r}  command not found : {y}{op_intarface}")
if __name__ == "__main__":
    S_T()
