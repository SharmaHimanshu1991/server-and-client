#!/usr/bin/python2

import socket,time
# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip= "192.168.10.199"

port=8888

while True:
	msg = raw_input ( "type your msg: ")
	# sendto function bind it by default.
	
	s.sendto(msg ,(ip,port))
	time.sleep(2)
	print "msg send"

	# receiver from server
	t=s.recvfrom(40)
	#if time.sleep(3):   #
	#	s.sendto(msg ,(ip,port))  #
	
	print (" msg from server : " + t[0])

execfile('main_client.py')
	
	
