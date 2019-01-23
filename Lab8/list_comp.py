#Lab 8
#Name: Ajay Patel
#Section: 1

import math


class Point:
   #attributes: x and y coordinates
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __repr__(self):
      return 'Point({:.2f}, {:.2f})'.format(self.x, self.y)


class Circle:
   #attributes: center point and radius
   def __init__(self, c, r):
       self.center = c
       self.radius = r

   def __repr__(self):
       return 'Center(({:.2f}, {.2f:}), {:.2f})'.format(center.x, center.y, radius)


def distance(Point1, Point2):
    #Compute distance between 2 points
    #(int, int) (int, int) -----> float or int
    x1 = Point1.x
    y1 = Point1.y
    x2 = Point2.x
    y2 = Point2.y
    diffx = (x1 - x2)**2
    diffy = (y1 - y2)**2
    dist = math.sqrt(diffx + diffy)


def circles_overlap(Circle1, Circle2):
    #Compute whether or not 2 circles overlap
    #((int, int), radius), ((int, int), radius) ----> true or false
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


def distance_all(L):
    #Compute the distance of each point in a list to the origin
    #list ----> list 
    distlist = map(lambda x: math.sqrt(x[0]**2 + x[1]**2), L)
    return list(distlist)


def are_in_first_quadrant(L):
    #Filter an input list to only have positive x and y components
    #list ---> list
    filterlist = filter(lambda x: x[0] > 0 and x[1] > 0, L)
    return list(filterlist)
