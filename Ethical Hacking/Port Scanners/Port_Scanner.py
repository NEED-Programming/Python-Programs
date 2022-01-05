# This code does a port/ports scan for a remote host# This will serially check the ports in a for loopimport socket
import pyfiglet
from pyfiglet import Figlet
import socket
import time
from datetime import datetime
import errno
import sys
import threading
from queue import Queue



# Banner
print("*" * 50)
ascii_banner = pyfiglet.figlet_format("NEED PORT SCANNER")
print(ascii_banner)
print("*" * 50)
print("-" * 50)
# here we asking for the target website / host
target = input('What IP/Domain do you want to scan?: ')
print("-" * 50)

print("$" * 50)
print("Scanning Target: {}".format(target))
print("Scanning started at:" + str(datetime.now()))
print("$" * 50)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# next line gives us the ip address of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

# function for scanning ports
def port_scan(port):
	try:
		s.connect((target_ip, port))
		return True
	except:
		return False


start = time.time()

# here we are scanning port 0 to whatever you desire
for port in range(0, 100):
	if port_scan(port):
		print(f'port {port} is open')
	else:
		print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')

def verbose(*args, **kwargs): print(*args, **kwargs)
verbose = True

def threader():
	while True:
		worker = q.get()
		port_scan(worker)
		q.task_done()

q = Queue()

for x in range(30):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()
q.join()