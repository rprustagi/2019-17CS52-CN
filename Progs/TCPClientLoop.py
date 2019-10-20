#!/usr/bin/python
#TCP client program
import sys
from socket import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="Server IP address", type = str, 
  dest = "servername", default="127.0.0.1")
parser.add_argument("--port", help = "Server port number",
  type = int, dest = "serverport", required = True)

args = parser.parse_args()
server = args.servername
port = args.serverport
recvsize = 2048

# create a socket and connect to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server, port))

while True:
    # get the data from user via stdin
    print ("Input in lower case sentence: ")
    sndmsg = input('type Exit to quit:\n')
    if sndmsg.lower() == "exit":
        break
    sndmsg = sndmsg.encode('ascii')
    clientSocket.send(sndmsg)
    recdMessage = clientSocket.recv(recvsize)
    recdMessage = recdMessage.decode('ascii')
    print ("Received from server: ", recdMessage)
clientSocket.close()
