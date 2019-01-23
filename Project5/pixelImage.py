#Project 5
#Names: Haley Childress and Ajay Patel
#Instructor: S. Einakian
#Section: 1

from Puzzle import puzzle
from fade import fade
from blur import blur


import sys 

args = sys.argv 

def main():

   if len(args) == 2:
      puzzle() 
   elif len(args) == 5:
      fade()
   elif len(args) == 3:
      blur()
   else:
      print('Error: Incorrect Number of Arguments')

if __name__ == '__main__':
   main()
