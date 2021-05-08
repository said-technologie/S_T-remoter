#this a random tips wich will be printed in the terminal
#import modules
import time , os , sys
import random
#colors variabals
g = "\033[32m"
y = "\033[33m"
r = "\033[31m"
v = "\033[35m"
none = "\033[0m"
#def function for the tips

def tips():
    tips_list = [f"type {g}help {v}to show the help menu{none}",f"you can use the {g}usage {v}command to find same info about auther commands{none}",f"{v}you can check your internet connection by typing {g}get status{none}"]
    ran_print = random.choice(tips_list)
    print(f" {g}                Tips {y}>> {v}{ran_print}{v}")
tips()