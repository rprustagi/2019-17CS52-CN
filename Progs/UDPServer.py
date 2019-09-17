#!/usr/bin/python
#UDP server program
import sys
import argparse
from socket import *

recvSize = 2048

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="Listening IP address", type = str, 
  dest = "servername", default = "0.0.0.0")
parser.add_argument("--port", help = "Listening port number",
  type = int, dest = "serverport", required = True, default=9999)

args = parser.parse_args()
serverName = args.servername
serverPort = args.serverport

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print ("UDP Server ready to receive data on port = ",  serverPort)
while 1:
  message, clientAddr = serverSocket.recvfrom(recvSize)
  message = message.decode('ascii')
  print ("Received from ", clientAddr, " data: ", message)
  respMsg = message.upper().encode('ascii')
  serverSocket.sendto(respMsg, clientAddr)
