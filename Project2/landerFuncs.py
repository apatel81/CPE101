#Project 2 - Moonlander Functions
#Name: Ajay Patel
#Professor: S. Einakian
#Section: 1

def showWelcome():
   #Display welcome message
   #none -> str
   print('')
   print('Welcome aboard the Lunar Module Flight Simulator')
   print('')
   print("   To begin you must specify the LM's initial altitude") 
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print('')
   print('   Good luck and may the force be with you!')

def getFuel():
   #Ask user for a positive integer and return it
   #None -> int
   num = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   while num<1:
      print ('ERROR: Amount of fuel must be positive, please try again')
      num = int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   return num
  
def getAltitude():
   #Ask user for an initial altitude
   #None -> int
   num = int(input('Enter the initial altitude of the LM (in meters): '))
   while num<1 or num>9999:
      print ('ERROR: Altitude must be between 1 and 9999, inclusive, please try again')
      num = int(input('Enter the initial altitude of the LM (in meters): '))
   return num

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    #Display the elapsed time, altitude, velocity, fuel amount, and fuel rate
    #Statements -> value
    print ("Elapsed Time:" + '{:5d}'.format(elapsedTime) + " s")    
    print ("        Fuel:" + '{:5d}'.format(fuelAmount) + " l")  
    print ("        Rate:" + '{:5d}'.format(fuelRate) + " l/s")   
    print ("    Altitude:" + '{:8.2f}'.format(altitude) + " m")
    print ("    Velocity:" + '{:8.2f}'.format(velocity) + " m/s")

def getFuelRate(currentFuel):
   #Ask the user for the desired fuel rate
   #None -> int
   print ("")
   num  = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while num<0 or num>9:
       print ("ERROR: Fuel rate must be between 0 and 9, inclusive") 
       num = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if num<currentFuel:
       return num
   elif num>=currentFuel:
       return currentFuel

def updateAcceleration(gravity, fuelRate):
   #Calculate current acceleration using gravity and current fuel rate
   #float int -> float
   acceleration = gravity * ((fuelRate/5)-1)
   return acceleration	

def updateAltitude(altitude, velocity, acceleration):
   #Calculate current altitude using old altitude, old velocity, and current acceleration
   #int float float -> float
   newaltitude = altitude + velocity + (acceleration/2)   
   return newaltitude

def updateVelocity(velocity, acceleration):
   #Calculate current velocity using old velocity and current acceleration
   #float float -> float
   newvelocity = velocity + acceleration
   return newvelocity

def updateFuel(fuel, fuelRate):
   #Calculate remaining fuel using old fuel remaining and current fuel rate
   #int int -> int
   newfuel = fuel - fuelRate
   return newfuel
   
def displayLMLandingStatus(velocity):
   #Display landing status message based on final velocity
   #float -> str
   if velocity>=-1.0 and velocity<=0.0:
      print("Status at landing - The eagle has landed!")
   elif velocity<-1.0 and velocity>-10.0:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity<=-10.0:
      print("Status at landing - Ouch - that hurt!")
