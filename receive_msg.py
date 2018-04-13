#!/usr/bin/python2

import socket,time
import sys

#print(sys.argv)
# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



ip= "192.168.10.199"

port=8888

s.bind((ip,port))


while True:
	
	data=s.recvfrom(40)
	print ("receive from client: " + data[0])
	
	# send to client
	reply = raw_input(" reply to sender: " )
	#a=sys.argv(reply[0])
	#print a
	#t= time.sleep(3)
	#print t
	#if reply == a:
	#	s.sendto('0',data[1])
	#else:
		
	s.sendto(reply ,data[1])
	
