#Lab 5
#Name: Ajay Patel
#Section 1

import unittest
import filter

class TestCases(unittest.TestCase):
   def test_are_positive(self):
       list1 = [-4, 1, -9, 5, 8]
       list2 = [-39, 37, 29, 876, -23]       
       self.assertListEqual(filter.are_positive(list1), [1, 5, 8])
       self.assertListEqual(filter.are_positive(list2), [37, 29, 876])

   def test_are_greater_than_n(self):
       list1 = [3, 6, 4, 8, 12, 21]
       list2 = [5, -14, 9, 16, 7]
       self.assertListEqual(filter.are_greater_than_n(list1, 5), [6, 8, 12, 21])
       self.assertListEqual(filter.are_greater_than_n(list2, 8), [9, 16])

   def test_are_dividable_by_n(self):
       list1 = [2, 5, 7, 10, 12]

       self.assertListEqual(filter.are_dividable_by_n(list1, 2), [2, 10, 12]) 

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
