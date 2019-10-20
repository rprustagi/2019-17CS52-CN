#!/usr/bin/python
#TCP server program
import sys
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="Server IP address", type = str, 
  dest = "servername", default="0.0.0.0")
parser.add_argument("--port", help = "Server port number",
  type = int, dest = "serverport", required = True)

args = parser.parse_args()
server = args.servername
port = args.serverport
recvsize = 2048

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((server, port))
serverSocket.listen(1); # change the value to higher number and study impact

print ("TCP Server ready to receive data on port = ", port)
while True:
    connSocket, clientAddr = serverSocket.accept()
    print ("Accepted new Connection from ", clientAddr)
    message = connSocket.recv(recvsize)
    message = message.decode('ascii')
    while (len(message)!= 0):
        print ("Received data: ", message)
        respMsg = message.upper()
        respMsg = respMsg.encode('ascii')
        connSocket.send(respMsg)
        message = connSocket.recv(recvsize)
        message = message.decode('ascii')
    connSocket.close()
