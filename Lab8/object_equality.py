#Lab 8
#Name: Ajay Patel
#Section: 1

import math
from utility import*

class Point:
   #attributes: x and y coordinates
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __repr__(self):
      return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)
 
   def __eq__(self, other):
       checkx = epsilon_equal(self.x, other.x)
       checky = epsilon_equal(self.y, other.y)
       return (checkx, checky)


class Circle:
   #attributes: center point and radius
   def __init__(self, c, r):
       self.center = c
       self.radius = r

   def __repr__(self):
       return 'Center(({:.2f}, {.2f:}), {:.2f})'.format(center.x, center.y, radius)


def distance(Point1, Point2):
    Point1.x = x1
    Point1.y = y1
    Point2.x = x2
    Point2.y = y2
    diffx = (x1 - x2)**2
    diffy = (y1 - y2)**2
    dist = math.sqrt(diffx + diffy)


def circles_overlap(Circle1, Circle2):
    Circle1.x = x1
    Circle1.y = y1
    Circle2.x = x1
    Circle2.y = y2
    Circle1.c = center1
    Circle2.c = center2
    Circle1.r = radius1
    Circle2.r = radius2
    diffx = (x1 - x2)**2
    diffy = (y1 - y2)**2
    dist = math.sqrt(diffx + diffy)
    rsum = radius1 + radius2
    a = bool(rsum > dist)



