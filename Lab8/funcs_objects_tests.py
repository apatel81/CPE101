#Lab 8 
#Name: Ajay Patel
#Section

import unittest
#import objects
from objects import *

class TestCases(unittest.TestCase):

   def test_Point(self):
       p1 = Point(1,2)
       p2 = Point(3,4)
       self.assertEqual(p1.x, 1)
       self.assertEqual(p1.y, 2)
       self.assertEqual(p2.x, 3)
       self.assertEqual(p2.y, 4)


   def test_Circle(self):
       center1 = Point(1,1)
       center2 = Point(3.6, 2.1)
       radius1 = 3
       self.assertEqual(center1.x, 1)
       self.assertEqual(center1.y, 1)
       self.assertEqual(center2.x, 3.6)
       self.assertEqual(center2.y, 2.1)
       self.assertEqual(radius1, 3)  


   def test_distance(self):
       p1 = Point(0,0)
       p2 = Point(4,3) 
       self.assertEqual(math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2), 5)
       p3 = Point(1,2)
       p4 = Point(3, 9)
       self.assertEqual(math.sqrt((p3.x - p4.x)**2 + (p3.y - p4.y)**2), 7.280109889280518)


   def test_circles_overlap(self):
       center1 = Point(0,0)
       center2 = Point(5,5)
       center3 = Point(1,1)
       r1 = 3
       r2 = 4
       r3 = 20
       self.assertTrue((bool(math.sqrt((center1.x - center2.x)**2 + (center1.y - center2.y)**2)>(r1 + r2)), True))
       self.assertTrue((bool(math.sqrt((center3.x - center1.x)**2 + (center3.y - center1.y)**2)>(r1 + r1)), False))




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

