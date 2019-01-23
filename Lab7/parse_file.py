#Lab 7
#Name: Ajay Patel
#Section 1

import sys
args = sys.argv

if len(args) == 2:
   filename = args[1]
   try:
      fin = open(filename, 'r')
      t = []
      for line in fin:
          s = line.split()
          for elements in s:
              t.append(elements)
      ints = 0
      floats = 0
      other = 0
      for i in range(len(t)):       
          if t[i].isdigit() == True:
             ints += 1
          else:
            try:
              float(t[i])
              floats += 1 
            except:
              other += 1
      
      print('Ints:',ints)
      print('Floats:',floats)
      print('Other:',other)

   except:  
      print('Unable to open ' + filename)


elif len(args) == 3:
   if args[2] == '-s':
      filename = args[1]
      try:
         fin = open(filename, 'r')
         t = []
         for line in fin:
             s = line.split()
             for elements in s:
                 t.append(elements)
         ints = 0
         floats = 0
         other = 0
         sum1 = 0
         sum2 = 0
         sum3 = 0
         for i in range(len(t)):
             if t[i].isdigit() == True:
                sum1 += int(t[i])
                ints += 1
             else:
                try:
                   float(t[i])
                   sum2 += float(t[i])
                   floats += 1
                except:
                   other += 1
 
         sum3 = sum1 + sum2
         print('Ints:',ints)
         print('Floats:',floats)
         print('Other:',other)
         print('Sum:',sum3) 

      except:
         print('Unable to open ' + filename)
   
   elif args[1] == '-s':
      filename = args[2]
      try:
         fin = open(filename, 'r')
         t = []
         for line in fin:
             s = line.split()
             for elements in s:
                 t.append(elements)
         ints = 0
         floats = 0
         other = 0
         sum1 = 0
         sum2 = 0 
         sum3 = 0
         for i in range(len(t)):
             if t[i].isdigit() == True:
                sum1 += int(t[i])
                ints += 1
             else:
               try:
                 float(t[i])
                 sum2 += float(t[i])
                 floats += 1
               except:
                 other += 1
         
         sum3 = sum1 + sum2
         print('Ints:',ints)
         print('Floats:',floats)
         print('Other:',other)
         print('Sum:',sum3)  

      except: 
         print('Unable to open ' + filename)     

   else:
       print('Usage: [-s] file_name') 
       exit()
else:
    print('Usage: [-s] file_name')
    exit() 




def commandline(filename, flag):
    pass
    
    

