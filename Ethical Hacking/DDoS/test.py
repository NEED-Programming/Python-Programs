
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.google.com')
print(ip)


portInvalid = True
port = input("PORT:")

while portInvalid:
    try:
        port = int(port)
        portInvalid = False
    except ValueError:
        port = input("please enter a valid port number:")
