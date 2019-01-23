#Lab8
#Name: Ajay Patel
#Section: 1


import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   def test_distance_all(self):
       list1 = [(1,1), (2,2), (3,3)]
       list2 = [(3,4), (5,12), (6,8)]
       self.assertEqual(distance_all(list1), [1.4142135623730951, 2.8284271247461903, 4.242640687119285])
       self.assertEqual(distance_all(list2), [5, 13, 10])


   def test_are_in_first_quadrant(self):
       list1 = [(-2,3), (4,6), (9,-8), (5,5)]
       list2 = [(1,1), (-2,-2), (3,3), (4, -5), (7,8)]
       self.assertEqual(are_in_first_quadrant(list1), [(4,6), (5,5)])
       self.assertEqual(are_in_first_quadrant(list2), [(1,1), (3,3), (7,8)])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

