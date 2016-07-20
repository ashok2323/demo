#!/usr/bin/python
import sys
import os

userallinput = sys.argv
print userallinput
print "number of arguement ", len(sys.argv)
print "arguement list :", str(sys.argv)

index = 0
for localvar in sys.argv:
        print "index" + str(index) + ":" + localvar
        if (localvar == "cow"):
             print "length of string 'cow' :",  len(localvar)
        else:
              print " i am not in mood to do anything"
        index = index + 1
 
num = 1
while num < 4:
      print num
      if (num == 4):
             print " loop completed "
      else:
          print " still have to long way "
      num = num + 1
print "done"

foldername = raw_input("plese provide for abosulte path:")
cmd = 'ls ' + foldername + ' >/tmp/output'
print cmd
outputcd = os.system(cmd)
if (outputcd != 0):
          print " path does not exist"
          exit
txt = open('/tmp/output')
myindex = 0
for myfile in txt:
      print "filename : ", myfile
      myindex = myindex + 1


