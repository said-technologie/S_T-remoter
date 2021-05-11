#here is all the def functions that will be use by S_T-remoter
# v1.0
'''seting cloros variables'''

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[0m"
'''version of the tool'''
version = "1.0"
'''importing the modules'''

import os , sys , time
import requests
from webbrowser import *
import platform
'''def functions'''

def help_menu():
    print(f"    {r} commands                    {c} description                                                   {g}example")
    print(f"    {y}   help          {g}>>{r}   [{v}       it will show this help menu                         {r}]")
    print(f"    {y}   clear         {g}>>{r}   [{v}        it will clear the terminal                         {r}]")
    print(f"    {y}   exit          {g}>>{r}   [{v}          use it to exit the tool                          {r}]")
    print(f"    {y}   usage         {g}>>{r}   [{v} it will show how you can the commands of te toll          {r}]{y}            usage {g}<start server>{g}")
    print(f"    {y}   update        {g}>>{r}   [{v}            it will update the toll                        {r}]")
    print(f"    {y}   get status    {g}>>{r}   [{v} it will check if you are connected to the internet ro not {r}]")
    print(f"    {y}  exploit-payload{g}>>{r}   [{v}         it will creat a python malware                    {r}]{y}            exploit-payload {g}<Linux , Termux , Windows>{none} ")
    print(f"    {y}   start server  {g}>>{r}   [{v}     it will start a server for the malware                {r}]")
    print(f"    {y}   cre_channel   {g}>>{r}   [{v} it will show you the creator of this tool channels        {r}]{y}            cre_channel {r}-c {g}<Github , Youtube , Facebook>{r} -o {g} <Termux , Linux , Windows , Mac>")

'''making a python payload that alaws the hacker to make a connection with his victim'''
class exploit_payload:
    '''exploit paylaod for Linux'''
    def exploit_payload_Linux():
        paylaod_name = input(f"{c}[{y}!{c}]  {v}enter {r}payload {v}name {r}: {g}")
        time.sleep(2)
        print(f"  {v}[{y}!{v}] {y}making the {r}payload{y} ...")
        os.system(f"touch ../payloads/Linux/{paylaod_name}.py")
        payload_file = open(f"../payloads/Linux/{paylaod_name}.py","w")
        payload_file.write("")
        payload_file.close()
        print(f"  {c}[{g}+{c}] {g}payload saved to {y}/payloads/Linux/{paylaod_name}.py")
    '''exploit paylaod for  Termux'''
    def exploit_payload_Termux():
        paylaod_name = input(f"{c}[{y}!{c}]  {v}enter {r}payload {v}name {r}: {g}")
        time.sleep(2)
        print(f"  {v}[{y}!{v}] {y}making the {r}payload{y} ...")
        os.system(f"touch ../payloads/Linux/{paylaod_name}.py")
        payload_file = open(f"../payloads/Termux/{paylaod_name}.py","w")
        payload_file.write("")
        payload_file.close()
        print(f"  {c}[{g}+{c}] {g}payload saved to {y}/payloads/Termux/{paylaod_name}.py")
    '''exploit paylaod for  Windows'''
    def exploit_payload_Windows():
        paylaod_name = input(f"{c}[{y}!{c}]  {v}enter {r}payload {v}name {r}: {g}")
        time.sleep(2)
        print(f"  {v}[{y}!{v}] {y}making the {r}payload{y} ...")
        os.system(f"touch ../payloads/Linux/{paylaod_name}.py")
        payload_file = open(f"../payloads/Windows/{paylaod_name}.py","w")
        payload_file.write("")
        payload_file.close()
        print(f"  {c}[{g}+{c}] {g}payload saved to {y}/payloads/Windows/{paylaod_name}.py")

'''making the cre_channel option'''

class channel:
        def youtube_T_L():
            if platform.system == "Linux":
                try:
                    os.system("xdg-open https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
                except:
                    os.system("temux-open https://www.youtube.com/channel/UCfD0KLgqBqvUzJsTGwqG1vQ")
        def github_T_L():
            if platform.system == "Linux":
                try:
                    os.system("xdg-open https://github.com/said-technologie")
                except:
                    pass
        def facebook_T_L():
            if platform.system == "Linux":
                try:
                    os.system("xdg-open https://www.facebook.com/Said_technologie-111339843954624")
                except:
                    pass

'''cheking the status of thes user'''

def status():
    git_repo = requests.get("https://github.com/said-technologie/S_T-remoter/blob/main/version.txt").status_code
    if git_repo == 200:
        print(f" {c}[{g}+{c}] {v} internet status {r}>> {g}Online")
    else:
        print(f" {c}[{r}!{c}] {v} internet status {r}>> {y}Ofline")

'''updating the toll in case there is an update'''

def git_repo():
    git_repo = requests.get("https://github.com/said-technologie/S_T-remoter/blob/main/version.txt").status_code
    if git_repo == 200:
        github_ver = git_repo.text()
        github_ver = github_ver.strip()
        if version == github_ver:
            print(f" {c}[{g}+{c} {v} there is no available updates")
        else:
            print(f" {c}[{g}+{c} {v} there is an available update")
            up_check = input(f" {c}[{y}?{c}] {y}do you want to update {g}y{v}/{r}n{y} : ")
            if up_cheke == "y":
                os.system("git pull > cache/update.txt")
                print(f" {c}[{g}+{c}] {g}repo have ben updated")
                print(f" {c}[{g}+{c}] {g}restart the toll to commit the changes")
                sys.exit()
    else:
        print(f" {c}[{r}!{c} {y} you need to connect to the internet to cheeke the update")

'''building a class for all the usage command'''

class usage:
    '''usage for get status command'''
    def usage_get_status():
        print(f"        {v}Usage {g}get status {r}:{none}")
        print(f"             {v} this command {r}'{g}get status{r}'{v} will alwas you to get your status will that means that it will print to you if you are {g}connected {v} or not{none}")
        print(f"        {y} Example {r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                  {g}get status{none}")
        print(f"             {c} output{r} :{none}")
        print(f"                  {c}[{g}+{c}]  {v}internet status {r}>> {g}Online{none}")
        print(f"                                {r}OR")
        print(f"                  {c}[{r}!{c}] {v} internet status {r}>> {y}Ofline{none}")
    '''usage for start server'''
    def usage_start_server():
        print(f"        {v}Usage {g}start server {r}:{none}")
        print(f"            {v} this command {r}'{g}start server{r}'{v} will alwas you to creat a server that will creat a connection between you and your {r}victim{v} so you can control his device remotly{none}")
        print(f"               {v}but first you need to type {r}'{g}exploit-pyload{r}'{v} to creat a python malware and you need to send it to your {r}victim{none}")
        print(f"        {y} Example {r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                 {g}start server{none}")
        print(f"             {c} output{r} :{none}")
        print(f"                 {c}[{y}!{c}] {g}starting a sever...{none}")
        print(f"                 {c}[{g}+{c}] {g}server started{none}")
        print(f"     {g}Tips{r}:{v} after you do that type {y}help{v} to show an auther help menu")
    '''usage for cre_channel'''
    def usage_cre_channel():
        print(f"        {v}Usage {g}cre_channel {r}:{none}")
        print(f"            {v} this command {r}'{g}cre_channel{r}'{v} will alaws you to see all my channls and even open it on a browser{v}{none}")
        print(f"                             {g}please {y}subscribe{g} to my {y} Youtube{g} channel")
        print(f"        {y} Example {g}for Linux{r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                    {y}1{r}-{v} Youtube{none}")
        print(f"                          {g}cre_channel -c Youtube -o Linux")
        print(f"                    {y}2{r}-{v} Github{none}")
        print(f"                          {g}cre_channel -c Github -o Linux")
        print(f"                    {y}3{r}-{v} Facebook{none}")
        print(f"                          {g}cre_channel -c Facebook -o Linux")
        print(f"        {y} Example {g}for Termux{r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                    {y}1{r}-{v} Youtube{none}")
        print(f"                          {g}cre_channel -c Youtube -o Termux")
        print(f"                    {y}2{r}-{v} Github{none}")
        print(f"                          {g}cre_channel -c Github -o Termux")
        print(f"                    {y}3{r}-{v} Facebook{none}")
        print(f"                          {g}cre_channel -c Facebook -o Termux")
        print(f"        {y} Example {g}for Windows{r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                    {y}1{r}-{v} Youtube{none}")
        print(f"                          {g}cre_channel -c Youtube -o Windows")
        print(f"                    {y}2{r}-{v} Github{none}")
        print(f"                          {g}cre_channel -c Github -o Windows")
        print(f"                    {y}3{r}-{v} Facebook{none}")
        print(f"                          {g}cre_channel -c Facebook -o Windows")
        print(f"        {y} Example {g}for Mac{r}:{none}")
        print(f"             {c} input{r} :{none}")
        print(f"                    {y}1{r}-{v} Youtube{none}")
        print(f"                          {g}cre_channel -c Youtube -o Mac")
        print(f"                    {y}2{r}-{v} Github{none}")
        print(f"                          {g}cre_channel -c Github -o Mac")
        print(f"                    {y}3{r}-{v} Facebook{none}")
        print(f"                          {g}cre_channel -c Facebook -o Mac")
        print(f"             {c} output{r} :{none}")
        print(f"                         {v}it will open my {y}channels")