#Lab 2 Functions
#Name:Ajay Patel
#Section:1

import math

def math_func1(x,y):
      # Compute the function math_func1  by passing 2 values and dividing 
      # x^3 + y^3 / 5x + 7
      # int int -> float
      sum1 = x**3 + y**3
      sum2 = 5*x + 7
      return sum1/sum2
   
def math_func2(a,b,c):
      # Compute the function math_func2  by passing 3 values and dividing 
      # (-b + sqrt(b^2 - 4ac)) to (2a)
      # int int int -> float
      sum1 = -b + math.sqrt((b**2) - 4*a*c )
      sum2 = 2*a
      return sum1/sum2 

def d(x1,y1,x2,y2):
      # Compute the function d by passing 4 values and square rooting
      # (x1-x2)**2 + (y1-y2)**2
      # int int int -> float
      sum1 = (x1-x2)**2
      sum2 = (y1-y2)**2
      return math.sqrt(sum1 + sum2)

def is_negative(a):
      # Compute the function is_negative 
      # int -> true or false
      num = a
      return bool(a)

def dividable_by_5(a):
      # Compute the function dividable_by_5
      # int -> true or false
      num = a
      return (a/5)

