#this is the setup file for the toll
#importing modules

import time, os, sys

#colors variables
g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[0m"
#the installation
os.system("clear")
time.sleep(2)
while True:
    op_check = input(f" {c}[{y}!{c}] {y} witch {g}os{y} you use {r}>>[{v} Termux {r}|{v} Linux {r}]<< {g} : {r}")
    if op_check == "Termux":
        print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
        time.sleep(2)
        print(f" {c}[{y}!{c}] {r}  updating and upgrading{none}")
        os.system("pkg update -y >> cache/install.txt && pkg upgrade -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  installing ssh{none}")
        os.system("pkg install ssh -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  updating python{none}")
        os.system("pkg install python3 -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  installing the needing modules{none}")
        os.system("pip3 install -r requirement.txt >> cache/install.txt")
        print(f" {c}[{g}+{c}] {g}  Done{none}")
        print(f" {c}[{g}+{c}] {g}  type {y} python3 S_t.py {none}")
        break
    elif op_check == "Linux":
        print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
        time.sleep(2)
        print(f" {c}[{y}!{c}] {r}  updating and upgrading{none}")
        os.system("sudo apt-get update -y >> cache/install.txt && sudo apt-get upgrade -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  installing ssh{none}")
        os.system("sudo apt-get install ssh -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  updating python{none}")
        os.system("sudo apt-get install python3 -y >> cache/install.txt")
        print(f" {c}[{y}!{c}] {r}  installing the needing modules{none}")
        os.system("pip3 install -r requirement.txt >> cache/install.txt")
        print(f" {c}[{g}+{c}] {g}  Done{none}")
        print(f" {c}[{g}+{c}] {g}  type {y} python3 S_t.py {none}")
        break
    else :
        print(f" {c}[{r}!{c}] {y} you have to choose an os from {g} Termux {y}or {g}Linux")