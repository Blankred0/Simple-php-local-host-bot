import subprocess
import time
import random

# Tool-made-by-https://github.com/Blankred0
random_ports = random.randint(1024, 65536)
print("Ports aléatoires :", random_ports)
cmd2 = "clear"
loop = "N"
server_start = "php -S localhost:" + str(random_ports)
server_end = subprocess.Popen(server_start, shell=True)
time.sleep(1)
Link = ("Link : http://localhost:" + str(random_ports))

while loop == "N":
	print (Link)
	loop = input("Press [Enter] to stop server\n Press [C] to clear the terminal\n :")
	if loop == "C" :
		cmd3 = subprocess.Popen(cmd2, shell=True)
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