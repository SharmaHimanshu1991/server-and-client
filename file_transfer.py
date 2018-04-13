#!/usr/bin/python2
import os

fo = open("foo.txt", "r+")
#print fo

fo4 = fo.read(2)
print fo4
print type(fo4)
print ("*************")
#fo = open("foo.txt", "r+")
fo1= fo.readline(22)
print fo1
fo2 = fo.readlines()
print fo2
#fd= os.path.join(os.getcwd(),"file.txt")
#print fd



