# This code does a port/ports scan for a remote host# This will serially check the ports in a for loopimport socket
import pyfiglet
import socket
import time
from datetime import datetime
import errno
import sys

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Banner
print("-" * 50)
print("Scanning Target: ")
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# here we asking for the target website
# or host
target = input('What you want to scan?: ')

# next line gives us the ip address
# of the target
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

# here we are scanning port 0 to 4
for port in range(1, 100):
	if port_scan(port):
		print(f'port {port} is open')
	else:
		print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')
