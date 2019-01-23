#Project 1
#
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

import funcs

def main():

     mass = funcs.poundsToKG(float(input("How much do you weigh (pounds)? ")))    
     distance = float(input("How far away is your professor (meters)? "))   
     object = str(input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? "))

     velskater = float(funcs.getVelocitySkater(mass, funcs.getMassObject(object), funcs.getVelocityObject(distance)))

#If statements

     if funcs.getMassObject(object) <=0.1:
       print ('\n' + "Nice throw! You're going to get an F!")
     elif funcs.getMassObject(object) >0.1 and funcs.getMassObject(object) <=1.0:
       print ('\n' + "Nice throw! Make sure your professor is OK.")
     else:
        if distance <20.0:
            print ('\n' + "Nice throw! How far away is the hospital?")
        if distance >=20.0:
            print ('\n' + "Nice throw! RIP professor.")
          
        print("Velocity of skater: " + (str("%.3f"%funcs.getVelocitySkater(mass,funcs.getMassObject(object), funcs.getVelocityObject(distance))) + " m/s"))       
   
        if velskater == 0.000:
          print ('\n' + " ")
        elif velskater>0.000 and velskater<0.2:
          print ('\n' + "My grandmother skates faster than you!")
        elif velskater>=0.2 and velskater<1.0:
          print (" ")
        else:
          print ('\n' + "Look out for that railing!!!")
 

if __name__ == '__main__':
   main()
