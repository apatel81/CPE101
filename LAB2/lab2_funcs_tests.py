#Lab 2 Test Cases
#Name: Ajay Patel
#Section: 1
import unittest
import funcs

class TestLab2(unittest.TestCase):
  
 def test_math_func1(self):
      self.assertAlmostEqual(funcs.math_func1(2,2), 0.94117647)
      self.assertAlmostEqual(funcs.math_func1(3,3), 2.45454545)

 def test_math_func2(self):
      self.assertEqual(funcs.math_func2(1,2,1), -1)
      self.assertAlmostEqual(funcs.math_func2(5,-6,1), 1) 

 def test_d(self):
      self.assertAlmostEqual(funcs.d(1,1,2,2), 1.41421356)
      self.assertAlmostEqual(funcs.d(6,6,3,2), 5)
 
 def test_is_negative(self):
      self.assertTrue(funcs.is_negative(2), True)
      self.assertTrue(funcs.is_negative(-3), False)

 def test_dividable_by_5(self):
      self.assertTrue(funcs.dividable_by_5(10), True)
      self.assertTrue(funcs.dividable_by_5(12), False)
    
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
