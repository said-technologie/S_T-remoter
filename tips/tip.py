#this a random tips wich will be printed in the terminal
#import modules
import time , os , sys
import random
#colors variabals
g = "\033[32m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"
#def function for the tips

def tips():
    tips_list = [f"type {g}help {none}to show the help menu",f"you can use the {g}usage {none}command to find same info about auther commands",f"your can cheke you internet connection by typing {g}get status{none}"]
    ran_print = random.choice(tips_list)
    print(f" {r}                Tips {y}>> {none}{ran_print} {none}")
