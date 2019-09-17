#!/usr/bin/python
#UDP client program
import sys
import argparse
from socket import *

recvSize = 2048

parser = argparse.ArgumentParser()
parser.add_argument("--server", help="Server IP address", type = str, 
  dest = "servername", required=True)
parser.add_argument("--port", help = "Server port number",
  type = int, dest = "serverport", required = True)

print(sys.argv)
args = parser.parse_args()
serverName = args.servername
serverPort = args.serverport


clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input in lower case sentence:')
clientSocket.sendto(message.encode('ascii'), (serverName, serverPort))
recdMessage, serverAddress = clientSocket.recvfrom(recvSize)
print (recdMessage.decode('ascii'))

message = input('Input in lower case sentence:')
clientSocket.sendto(message.encode('ascii'), (serverName, serverPort))
recdMessage, serverAddress = clientSocket.recvfrom(recvSize)
print (recdMessage.decode('ascii'))

clientSocket.close()
