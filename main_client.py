#!/usr/bin/python2

from  time  import  sleep
print  "########################################################"
print  "########################################################"
print  "                                                        "
sleep(2)

options='''
Press 1  to  Chatting 
Press 2  to  Check the command :    
Press 3  to  Transfer the file data : 
Press q  to  close the programe :
'''

print  options
#  below function used for taking input from user 
choice=raw_input()

if  choice  ==  '1':

	execfile('send_msg.py')
	#  this function for calling  another file

elif  choice == '2':
	execfile('client.command.py')

elif  choice ==  '3':
	
	execfile('client_file.py')
else :
	exit()

