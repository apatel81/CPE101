#Project 5 - Image File Format
#Name: Haley Childress and Ajay Patel
#Instuctor: S. Einakian
#Section 1

import sys
args = sys.argv
 
def puzzle():
 if len(args) == 2:
   imagefilename = args[1]
   try:
      fin = open(imagefilename, 'r')
      t = []
      for line in fin:
          s = line.split()
          for elements in s:
              t.append(elements)
   
      i = 4
      group3list = []
      while i < len(t):
         three = t[i:i+3]
         i += 3
         group3list.append(three)

      hiddenlist = []
      for elements in group3list:
          newred = (int(elements[0])*10)
          newgreen = newred
          newblue = newred      
          if newred > 255:
             newred = 255
          else: 
             newred = (newred)
          if newgreen > 255: 
             newgreen = 255
          else:
             newgreen = newgreen
          if newblue > 255:
             newblue = 255
          else: 
             newblue = newblue
          hiddenlist.append(str(newred))
          hiddenlist.append(str(newgreen))
          hiddenlist.append(str(newblue))

      
      finout = open('hidden.ppm', 'w')
      finout.write(t[0] + '\n')
      finout.write(t[1] + '\n')
      finout.write(t[2] + '\n')
      finout.write(t[3] + '\n')
      for line in hiddenlist:
          #print(line)
          #line = line.rstrip()
          #print(type(line))
          finout.write(line + "\n")
      finout.close()
        

   except:
      print('Unable to open ' + imagefilename)

 else: 
   print('Usage: python puzzle.py image_file.ppm')


if __name__ == '__main__':
   puzzle()
