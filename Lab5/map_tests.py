#Lab 5
#Name: Ajay Patel
#Section 1

import unittest
import map

class TestCases(unittest.TestCase):

   def test_square_all(self):
     list1 = [2, 3, 4]
     list2 = [5, 6, 7]
     self.assertListEqual(map.square_all(list1), [4, 9, 16])
     self.assertListEqual(map.square_all(list2), [25, 36, 49])     

   def test_add_n_all(self):
     list1 = [2,4,6,8]
     list2 = [1, 3, 5]     
     self.assertListEqual(map.add_n_all(list1, 3), [5, 7, 9, 11])
     self.assertListEqual(map.add_n_all(list2, 5), [6, 8, 10])

   def test_even_or_odd_all(self):
     list1 = [1,2,3,4]
     list2 = [22, 76, 83, 91]
     self.assertListEqual(map.even_or_odd_all(list1), [False, True, False, True])
     self.assertListEqual(map.even_or_odd_all(list2), [True, True, False, False])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

