
#Lab3
#Name: Ajay Patel
#Section: 1

import unittest
import logic

class TestCases(unittest.TestCase):

  def test_is_even(self): 
    self.assertTrue(logic.is_even(10), True)
    self.assertFalse(logic.is_even(3), False)
    self.assertTrue(logic.is_even(4), True)

  def test_in_an_interval(self):
    self.assertFalse(logic.in_an_interval(-10), False)
    self.assertTrue(logic.in_an_interval(0), True)
    self.assertFalse(logic.in_an_interval(9), False)
    self.assertTrue(logic.in_an_interval(20), True)
    self.assertTrue(logic.in_an_interval(122), True)
    self.assertTrue(logic.in_an_interval(127), True)
 
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

