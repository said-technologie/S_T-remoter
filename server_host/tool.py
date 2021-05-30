'''importing modules'''
import os , sys , time

'''colors'''
g = "\033[32m"
c = "\033[36m"
v = "\033[35m"
y = "\033[33m"
r = "\033[31m"
none = "\033[0m"

'''making a help menu'''
def help_menu_session():
	print(f"    {r} commands                    {c} descriptionprint")
	print(f"    {y}   help            {g}>>{r}   [{v}        it will show this help menu           	      {r}]")
	print(f"    {y}   clear           {g}>>{r}   [{v}         it will clear the terminal           	      {r}]")
	print(f"    {y}   exit            {g}>>{r}   [{v}    use it to exit the th server or stop it          {r}]")
	print(f"    {y}   show session    {g}>>{r}   [{v} it show a tabule that it haveall your target        {r}]")
	print(f"    {y}   connect         {g}>>{r}   [{v}         use to connect to your taget                {r}]")
	print(f"     {v}the connect command take one argument  {y}  connect <{c}number of the target{r}>> ")
	print(f"        {v} you can get the number of your target by using {g}show session {v} command")

def progressbar(it, prefix="", size=60, file=sys.stdout):
	count = len(it)
	def show(j):
		x = int(size*j/count)
		file.write("%s[%s%s] %i/%i\r" % (prefix, ">"*x, "-"*(size-x), j, count))
		file.flush()
	show(0)
	for i, item in enumerate(it):
		yield item
		show(i+1)
	file.write("\n")
	file.flush()