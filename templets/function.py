#here is all the def functions that will be use by S_T-remoter
# v1.0
#serting cloros variables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"

#importing the modules

import os , sys , time
from webbrowser import *
#def functions

def help_menu():
    print(f"    {r} commands                    {c} description                                            {g}example")
    print(f"    {y}   help          {g}>>{r}   [{v}       it will show this help menu                  {r}]")
    print(f"    {y}   clear         {g}>>{r}   [{v}        it will clear the terminal                  {r}]")
    print(f"    {y}   exit          {g}>>{r}   [{v}          use it to exit the tool                   {r}]")
    print(f"    {y}   usage         {g}>>{r}   [{v} it will show how you can the commands of te toll   {r}]{y}              usage {g}<start server>{g}")
    print(f"    {y}   start server  {g}>>{r}   [{v}     it will start a server for the malware         {r}]")
    print(f"    {y}   cre_channel   {g}>>{r}   [{v} it will show you the creator of this tool channels {r}]{y}              cre_channel {r}-c {g}<Github , Youtube , Facebook>{r} -o {g} <Termux , Linux , Windows , Mac>")
class channel:
    def youtube_T_L():
        os.system("xdg-open https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
    def youtube_W_M():
