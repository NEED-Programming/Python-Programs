#!bash/python
import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = ("Hello UDP Server", "utf-8")

bytesToSend = str.encode(message)

bufferSize = 1024

serverport = ("127.0.0.1", 8081)

s.sendto(bytesToSend, serverport)

s.close()