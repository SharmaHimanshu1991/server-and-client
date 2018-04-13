#!/usr/bin/python2
import os

import socket,time
# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip= "192.168.10.199"

port=8888

while True:
	msg = raw_input(" Enter your command : ")
	
	# sendto function bind it by default.
	s.sendto(msg,(ip,port))
	time.sleep(2)
	#print "msg send"
	
	# command output receiver from server
	t=s.recvfrom(100)
	#print (type(t[0]))
	#print (t)
	if t[0] == '':
		
		print ("command not found...")
	else :
		print (t[0])

execfile('main_client.py')
		
