#!bash/python
import socket
s = socket.socket()
print("Socket successfully created")


port = 8080

s.bind(('', port))
print("Socket binded to %s" %(port))

s.listen()
print("Socket is listening")

while True:

    c, addr = s.accept()
    print('Got connection from', addr)

    c.send('Thank you for connection'.encode())

    c.close()

    break