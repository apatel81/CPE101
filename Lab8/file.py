#Lab8
#Name: Ajay Patel
#Section: 1

import sys

args = sys.argv

filename = args[1]

try: 
   fin = open(filename, 'r')
   list = []
   linenumber = 0
   for line in fin: 
       print('Line' , linenumber,'(',(len(line) - 1),'chars',')',':', line)
       list.append(line)  
       linenumber += 1
   

except:
   print("Error")
