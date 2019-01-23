#Project 1
#
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

import unittest
import funcs

class TestProject1(unittest.TestCase):

 def test_poundsToKG(self):
      self.assertAlmostEqual(funcs.poundsToKG(140), 63.50288)
      self.assertAlmostEqual(funcs.poundsToKG(120), 54.43104)

 def test_getMassObject(self):
      self.assertAlmostEqual(funcs.getMassObject('t'), 0.1)
      self.assertAlmostEqual(funcs.getMassObject('q'), 0.0)
 
 def test_getVelocityObject(self):
      self.assertAlmostEqual(funcs.getVelocityObject(25), 11.0679718)
      self.assertAlmostEqual(funcs.getVelocityObject(45), 14.8492424)

 def test_getVelocitySkater(self):
      self.assertAlmostEqual(funcs.getVelocitySkater(50, 1, 10), 0.2) 
      self.assertAlmostEqual(funcs.getVelocitySkater(35, 2.5, 6), 0.4285714)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

