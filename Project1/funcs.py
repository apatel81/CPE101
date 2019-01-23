#Project 1
#
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

import math

def poundsToKG(pounds):
      # To convert weight of person in pounds to KGs
      # kilograms = pounds * 0.453592
      # int -> float
      sum1 = pounds
      return float(sum1 * 0.453592)

def getMassObject(object):
      # To calculate mass of object being thrown
      # variable -> float(input(value))
      if object  == 't':
         return 0.1

      elif object == 'p':
         return 1.0
   
      elif object == 'r':
         return 3.0

      elif object  == 'g':
         return 5.3

      elif object  == 'l':
         return 9.07
 
      else: 
         return 0.0     

def getVelocityObject(distance):
      # To calculate how fast the object being thrown hits the professor
      # given a certain distance
      # int -> float
      sum1 = float(math.sqrt((distance * 9.8)/2.0))
      return float(sum1)

def getVelocitySkater(massSkater, massObject, velObject):
      # To calculate the velocity of the skater after throwing
      # the object of choice
      # int int int -> float
      sum1 = float((massObject * velObject)/massSkater)
      return float(sum1)
