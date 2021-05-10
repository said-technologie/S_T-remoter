#this is the modules checkr
#import the sys module

import sys , time
import shutil
import platform
#colors vriables

g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[38m"

'''cheking the modules'''

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
'''installing the ngork'''
def ngrok_check():
	pkg = ["ngrok"]
	for i in pkg:
		pkgs = shutil.which(i)
		if pkgs == None:
			if platform.system == "Linux":
				if 'SUDO_UID' in os.environ.keys():
					print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
					time.sleep(2)
					print(f" {c}[{y}!{c}] {r}  installing ngrok...{none}")
					os.system("curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip >> cache/install.txt")
					os.system("sudo apt-get install unzip -y >> cache/install.txt")
					os.system("sudo unzip ngrok-stable-linux-amd64.zip")
				elif not 'SUDO_UID' in os.environ.keys():
					print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
					time.sleep(2)
					print(f" {c}[{y}!{c}] {r}  installing ngrok...{none}")
					os.system("curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip >> cache/install.txt")
					os.system("pkg install unzip -y >> cache/install.txt")
					os.system("unzip ngrok-stable-linux-amd64.zip")				
			elif platform.system == "Windows":
				print(f" {c}[{r}?{c}] {r}this tool dosn't suporte windows os")
				sys.exit()
		else:
			continue
ngrok_check()