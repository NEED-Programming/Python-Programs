#!bash/python
from queue import Queue
import socket
import threading
import pyfiglet
import datetime
from datetime import *
# Banner
ascii_banner = pyfiglet.figlet_format("NEED PORT SCANNER")
print(ascii_banner)
print("*" * 50)
target = input('What target do you want to scan?: ')
queue = Queue()
open_ports = []
print("*" * 50)
print("$" * 50)
print("Scanning Target: {}".format(target))
print("Scanning started at:" + str(datetime.now()))
print("$" * 50)


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def get_ports(mode):
    if mode == 1:
        for port in range (1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range (1, 49152):
            queue.put(port)
    elif mode == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input("Enter your ports (seperate by blank):")
        ports = ports.split()
        ports - list(map(int, ports))
        for port in ports:
            queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        #else:    if you want to see closed ports - remove hash/comment markers
            #print("Port {} is closed!".format(port))


def run_scanner(threads, mode):
    
    get_ports(mode)
    
    thread_list = []
    
    for t in range(threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    
    for thread in thread_list:
        thread.start()
    
    for thread in thread_list:
        thread.join()
        
    print("Open ports are:", open_ports)

# 100 is thread count
# 1 is the mode
run_scanner(100, 1)