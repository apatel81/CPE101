#Lab8 
#Name: Ajay Patel
#Section: 1

import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality(self):
       p1 = Point(0,0)
       p2 = Point(0,0)
       p3 = Point(1,0)
       p4 = Point(1.45, 2.37)
       p5 = Point(1.45, 2.37)
       self.assertTrue(p1.x == p2.x and p1.y == p2.y, True)
       self.assertTrue(p1.x != p3.x and p1.y == p3.y, False)
       self.assertTrue(p4.x == p5.x and p4.y == p5.y, True)
    







# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

