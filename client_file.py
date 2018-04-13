#!/usr/bin/python2
import os

import socket,time
# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip= "192.168.10.199"

port=8080

fo = open("foo.txt",'r')
f=fo.read()
print len(f)
for var in fo:
	# sendto function bind it by default.
	s.sendto(var ,(ip,port))
time.sleep(2)
print "msg send"

execfile('main_client.py')
