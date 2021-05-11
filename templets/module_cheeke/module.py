#this is the modules checkr
#import the sys module

import sys , time
import shutil
import platform
import importlib
import requests
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
	modules = ["socket","webbrowser","threading","queue","requests","shutil","tabulate"]
	for module in modules:
		try:
			importlib.import_module(module)
			print("\033[35m  ["+"\033[32m+"+"\033[35m]"+"\033[32m  the"+"\033[33m "+ module+"\033[32m module is installed"+"\033[37m")
		except:
			print("\033[35m  ["+"\033[31m!"+"\033[35m]"+"\033[33m"+"  enable to import the"+"\033[31m "+ module+"\033[33m module you need to download"+"\033[37m")
			sys.exit()
'''installing the ngork'''
def update():
	if platform.system == "Linux":
		url = "https://raw.githubusercontent.com/said-technologie/S_T-remoter/main/version.txt"
		req_url = requests.get(url)
		status_url = requests.status_code(req_url)
		if status_url == 200:
			version_req = req_url.text
			version_strip = version_req.strip()
			if version_strip == 2:
				try:
					print(f"  {c}[{g}!{c}] {g}update find{none}")
					print(f"  {c}[{y}!{c}] {y}updating{none}")
					time.sleep(2)
					os.system("git pull >> cache/update.txt")
					print(f"  {c}[{g}+{c}] {g}tool updated succesfuly{none}")
					print(f"  {c}[{g}!{c}] {g}please restart the tool to uplay the changes{none}")
					sys.exit()
				except:
					print(f"  {c}[{r}?{c}] {r}could not to update the tool{none}")

	'''pkg = ["ngrok"]
	for i in pkg:
		pkgs = shutil.which(i)
		if pkgs == None:
			if platform.system == "Linux":
				if 'SUDO_UID' in os.environ.keys():
					
				elif not 'SUDO_UID' in os.environ.keys():
					print(f" {c}[{g}+{c}] {y}prepare to install...{none}")
					time.sleep(2)
					print(f" {c}[{y}!{c}] {r}  installing ngrok...{none}")
									
			elif platform.system == "Windows":
				print(f" {c}[{r}?{c}] {r}this tool dosn't suporte windows os")
				sys.exit()
		else:
			continue
ngrok_check()'''