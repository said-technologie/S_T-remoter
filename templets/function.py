#here is all the def functions that will be use by S_T-remoter
# v1.0
#serting cloros variables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"
#version of the tool
version = "1.0"
#importing the modules

import os , sys , time
from webbrowser import open
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
        webbrowser.open("https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
    def github_T_L():
        os.system("xdg-open https://github.com/said-technologie")
    def github_W_M():
        webbrowser.open("https://github.com/said-technologie")
    def facebook_T_L():
        os.system("xdg-open https://www.facebook.com/Said_technologie-111339843954624")
    def facebook_W_M():
        webbrowser.open("https://www.facebook.com/Said_technologie-111339843954624")

def status():
    git_repo = requestes.get("https://github.com/said-technologie/S_T-remoter/blob/main/version.txt").status_code
    if git_repo == 200:
        print(f" {c}[{g}+{c} {v} internet status {r}>> {y}Online")
    else:
        print(f" {c}[{r}!{c} {v} internet status {r}>> {y}Ofline")
def git_repo():
    git_repo = requestes.get("https://github.com/said-technologie/S_T-remoter/blob/main/version.txt").status_code
    if git_repo == 200:
        github_ver = git_repo.text
		github_ver = github_ver.strip()

		if version == github_ver:
			print(f" {c}[{g}+{c} {v} there is no available updates")
		else:
			print(f" {c}[{g}+{c} {v} there is an available update")
	else:
		print(f" {c}[{r}!{c} {y} you need to connect to the internet to cheeke the update")
        
