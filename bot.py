from pystyle import *
import subprocess
import time
import random

try:
	import pyfiglet
except:
	print ("You must have pyfiglet install ! (pip install pyfiglet)")
	
red = Col.light_red

banner = pyfiglet.figlet_format("PHP\nLocalhost")


# Tool-made-by-https://github.com/Blankred0
random_ports = random.randint(1024, 65536)
print("Ports aléatoires :", random_ports)
cmd2 = "clear"
loop = "N"
subdomain =""
servelink = "ssh -R " + str(subdomain) + "80:localhost:" + str(random_ports) + " serveo.net"
server_start = "php -S localhost:" + str(random_ports)
server_end = subprocess.Popen(server_start, shell=True)
time.sleep(0.1)
Link = ("\nLocal link : http://localhost:" + str(random_ports))
subprocess.Popen(cmd2, shell=True)
time.sleep(0.1)

while True:
	print(Colorate.Vertical(Colors.blue_to_red, banner, 2))
	print (Link)
	loop = input("\n \nPress [Enter] to stop server\n Type [C] to clear the terminal\n Type [serveo] to expose to the internet\n :")
	loop = loop.lower()
	if loop == "c" :
		cmd3 = subprocess.Popen(cmd2, shell=True)
	elif loop == "serveo":
		choose_subdomain = input('Do you want to choose your subdomain ?\n [Y]es\n [N]o\n :')
		if choose_subdomain == "Y" :
			subdomain = input("Choose your subdomain :")
			subdomain = str(subdomain) + ":"
			servelink = "ssh -R " + str(subdomain) + "80:localhost:" + str(random_ports) + " serveo.net"
			serveo_end = subprocess.Popen(servelink, shell=True)
			time.sleep(5)
			serveo_end.wait()
		else :
			subdomain = ""
			servelink = "ssh -R " + str(subdomain) + "80:localhost:" + str(random_ports) + " serveo.net"
			print ("Starting serveo...")
			print ("Press ctrl + c to exit serveo")
			serveo_end = subprocess.Popen(servelink, shell=True)
			serveo_end.wait()
			subprocess.Popen(cmd2, shell=True)
	elif loop == "":
		print("Stopping server...")
		break
	else:
		print("You must enter a valid input !")
		loop = "N"
	time.sleep(0.01)
print ("Server end !")
# Stop the local php server
server_end.terminate()
