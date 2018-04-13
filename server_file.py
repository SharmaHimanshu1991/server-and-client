#!/usr/bin/python2

import socket
# 			IP4		UDP
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



ip= "192.168.10.199"

port=8080

s.bind((ip,port))

data=s.recvfrom(1024000)
print ("receive from client: " + data[0])
print len(data[0])

#file_name = raw_input(" enter file name : " )
fo = open("file_name.txt", "w+")
fo.writelines(data[0])
fo.close()


