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

ssock = socket(AF_INET, SOCK_STREAM)
ssock.bind((server, port))
ssock.listen(1)

print ("TCP Server ready to receive data")
while True:
    csock, caddr = ssock.accept()
    rcvmsg = csock.recv(recvsize)
    rcvmsg = rcvmsg.decode('ascii')
    print ("Received data: ", rcvmsg)
    sndmsg = rcvmsg.upper().encode('ascii')
    csock.send(sndmsg)
    csock.close()
