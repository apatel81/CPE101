#Lab 6
#Name: Ajay Patel
#Section 1

import unittest
#from fold import*
import fold

class TestCases(unittest.TestCase):
   
    def test_sumfunction(self):
        list1 = [1,2,3,4]
        list2 = [12,34, 94]
        self.assertEqual(fold.sumfunction(list1), 10)       
        self.assertEqual(fold.sumfunction(list2), 140)
 
    def test_index_of_smallest(self):
        list1 = [10, 2, [ 1, 9, 23], 3]
        list2 = [9,[3, 10, 98], 23, 7]
        self.assertEqual(fold.index_of_smallest(list1), 2)
        self.assertEqual(fold.index_of_smallest(list2), 1)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

