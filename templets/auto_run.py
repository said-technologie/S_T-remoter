import os 
import platform
def auto():
	os.system("touch S_T-remoter")
	auto_run_file = open("S_T-remoter","w")
	auto_run_file.write("cd && python3 S_T-remoter/S_T.py")
	auto_run_file.close()
	if platform.system == "Linux":
		try:
			os.system("cp S_T-remoter /usr/bin")
		except:
			os.system("sudo cp S_T-remoter /usr/bin")