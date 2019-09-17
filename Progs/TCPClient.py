#!/usr/bin/python
#TCP client program
import sys
from socket import *
import argparse

recvsize = 2048

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="Server IP address", type = str, 
  dest = "servername", required=True)
parser.add_argument("--port", help = "Server port number",
  type = int, dest = "serverport", required = True)

args = parser.parse_args()
server = args.servername
port = args.serverport

# create a socket and connect to server
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((server, port))

# get the data from user via stdin
sndmsg = input('Input in lower case sentence:')
sndmsg = sndmsg.encode('ascii')
sock.send(sndmsg)
rcvmsg = sock.recv(recvsize)
rcvmsg = rcvmsg.decode('ascii')
print("Received from server: ", rcvmsg)
sock.close()
