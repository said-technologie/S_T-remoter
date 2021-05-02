#this is the modules cheker
#import the sys module
import sys , time
#cheking the modules

modules = ["socket","colorama","threading","queue"]

def modules_cheke():
	print("\033[35m  ["+"\033[31m!"+"\033[35m]"+"\033[33m  cheking the modules...")
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




















"""
try:
	for cheke in modules:
   		from cheke import *
		print("\033[35m  ["+"\033[32m+"+"\033[35m]"+"\033[33m  cheking the modules....")
	   	time.sleep(3)
	   	print("\033[35m  ["+"\033[32m+"+"\033[35m]"+"\033[32m  Done")
	   	time.sleep(2)
	   	print("\033[35m  ["+"\033[32m+"+"\033[35m]"+f"\033[32m  the {cheke} module is installed"+"\033[37m")
	   	sys.exit()
except:
	print("\033[35m  ["+"\033[31m!"+"\033[35m]"+"\033[33m"+f"  enable to import the {cheke} module you need to download"+"\033[37m")
"""