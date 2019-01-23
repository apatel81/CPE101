#Lab 7
#Name: Ajay Patel
#Section 1

import groups
import unittest

class TestCases(unittest.TestCase):
 
    def test_groups_of_3(self):
        list1 = [1,2,3,4,5,6,7,8,9]
        list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
        list3 = [1,2,3,4,5,6,7,8]
        self.assertEqual(groups.groups_of_3(list1), [[1,2,3], [4,5,6], [7,8,9]])
        self.assertEqual(groups.groups_of_3(list2), [[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
        self.assertEqual(groups.groups_of_3(list3), [[1,2,3], [4,5,6], [7,8]])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


