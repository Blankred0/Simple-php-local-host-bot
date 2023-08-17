import subprocess
import time
import random

# Tool-made-by-https://github.com/Blankred0
random_ports = random.randint(1024, 65536)
print("Ports aléatoires :", random_ports)
cmd2 = "clear"
loop = "N"
servelink = "ssh -R 80:localhost:" + str(random_ports) + " serveo.net"
server_start = "php -S localhost:" + str(random_ports)
server_end = subprocess.Popen(server_start, shell=True)
time.sleep(1)
Link = ("\nLocal link : http://localhost:" + str(random_ports))

while loop == "N":
	print (Link)
	loop = input("\n \nPress [Enter] to stop server\n Type [C] to clear the terminal\n Type [serveo] to expose to the internet\n :")
	if loop == "C" :
		cmd3 = subprocess.Popen(cmd2, shell=True)
		loop = "N"
	elif loop == "serveo":
		print ("Starting serveo...")
		print ("Press ctrl + c to exit serveo")
		serveo_end = subprocess.Popen(servelink, shell=True)
		time.sleep(5)
		loop = "N"


		

	elif loop == "":
		print("Stopping server...")
	else:
		print("You must enter a valid input !")
		loop = "N"
	time.sleep(0.01)
print ("Server end !")
# Stop the local php server
server_end.terminate()
serveo_end.terminate()