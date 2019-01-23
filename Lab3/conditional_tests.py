#Lab3
#Name: Ajay Patel
#Section: 1

import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(10,2), 10)
      self.assertTrue(conditional.max_101(3,15), True)
      self.assertTrue(conditional.max_101(3,2), True)

   def test_case(self):
      self.assertEqual(conditional.max_of_three(10.5,1.7,4.3), 10.5)
      self.assertTrue(conditional.max_of_three(9.7,8.3,12.1), True)
      self.assertTrue(conditional.max_of_three(5.4,6.2,1.4), True)
   
   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(6), 5)
      self.assertTrue(conditional.rental_late_fee(17), True)
      self.assertTrue(conditional.rental_late_fee(25), True)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

