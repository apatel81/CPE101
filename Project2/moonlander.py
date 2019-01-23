#Project 2 - Moonlander
#
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

from ioTests import *

def main():
    
    showWelcome()
    print()

    altitude = getAltitude()    
    fuelAmount = getFuel()
    elapsedTime = 0
    velocity = 0.00
    fuelRate = 0
    gravity = 1.62

    print()

    print('LM state at retrorocket cutoff')
    displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

    while fuelAmount > 0 and altitude > 0:

       elapsedTime += 1         
      
       fuelRate = getFuelRate(fuelAmount)
   
       acceleration = updateAcceleration(gravity, fuelRate)    
       
       fuelAmount = updateFuel(fuelAmount, fuelRate)

       altitude = updateAltitude(altitude, velocity, acceleration)

       velocity = updateVelocity(velocity, acceleration)

       if altitude > 0:
             if fuelAmount > 0:
                 displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

       if altitude <= 0:
          print('')
          print('LM state at landing/impact')

          altitude = 0

          displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)

          print('')
          displayLMLandingStatus(velocity)
   
    while altitude > 0: 
       
       print ('OUT OF FUEL - '+ 'Elapsed Time:' + '{:4d}'.format(elapsedTime) + ' Altitude:' + '{:8.2f}'.format(altitude) + ' Velocity:' + '{:8.2f}'.format(velocity))

       fuelRate = 0
      
       elapsedTime += 1
              
       acceleration = updateAcceleration(gravity, fuelRate)
       
       altitude = updateAltitude(altitude, velocity, acceleration)
       
       velocity = updateVelocity(velocity, acceleration)
       
       if altitude <=  0:
          print('')
          print('LM state at landing/impact')
          
          elapsedTime += 0
          fuelAmount = 0
          fuelRate = 0
          acceleraiton = updateAcceleration(gravity, fuelRate)
          altitude = 0
          
          displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)     

          print('')
          displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()
