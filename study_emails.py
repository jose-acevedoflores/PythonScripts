'''
Created on Jul 15, 2013

@author: joseacevedo
'''
import sys
import string
import os

os.chdir("./resources/mailing_list")
i=0
list = open("/Users/joseacevedo/Desktop/list.txt","a")
for fileName in os.listdir("."):
    #newName =  string.replace(fileName, "booked_ ", "")
    #os.rename(fileName, fileName[:-4])
    #os.rename(fileName,newName )
    print fileName
    #list.write(fileName+";")
    #i = i +1

list.close()
print "Done: " + str(i) + " files converted"
    