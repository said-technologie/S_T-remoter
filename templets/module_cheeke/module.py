#this is the modules checkr
#import the sys module

import sys , time
import shutil

#colors vriables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"

#cheking the modules

def modules_check():
	print("\033[35m  ["+"\033[31m!"+"\033[35m]"+"\033[33m  cheking the modules...")
	modules = ["socket","webbrowser","threading","queue","requests","shutil"]
	for pkg in modules:
		impoting = ''
		try:
			importing = "import" + pkg
			importing
			print("\033[35m  ["+"\033[32m+"+"\033[35m]"+"\033[32m  the"+"\033[33m "+pkg +"\033[32m module is installed"+"\033[37m")
			time.sleep(2)
		except:
			print("\033[35m  ["+"\033[31m!"+"\033[35m]"+"\033[33m"+"  enable to import the"+"\033[31m "+pkg +"\033[33m module you need to download"+"\033[37m")
			sys.exit()
#installing the ngork
def ngrok_check():
	pkg = ["ngrok"]
	for i in pkg:
		pkgs = which(i)
		if pkgs == None:
			install_ngrok = input(f" {c}[{r}!{c}] {y}could to find {g}ngrok{y} you need to download it {v}do you want to download it now{g}y{r}/{g}n {c}>> ")
			if install_ngrok == "y":
				print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
				time.sleep(2)
				print(f" {c}[{y}!{c}] {r}  installing ngrok...{none}")
				os.system("curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip >> cache/install.txt")
				os.system("sudo apt-get install unzip -y >> cache/install.txt")
				os.system("sudo unzip ")
			elif install_ngrok == "n":
				pass
			else:
				print(f" {c}[{y}!{c} {r}error argument {y}you to type {g}y{y} or{g} n")
				return ngrok_check()