#Project 2
#Name: Ajay Patel
#S. Einakian
#Section 1

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):

   def test_updateAcceleration(self):
      self.assertAlmostEqual(updateAcceleration(1.62,5), 0)
      self.assertAlmostEqual(updateAcceleration(1.62,17), 3.888)
      self.assertAlmostEqual(updateAcceleration(1.62, 20), 4.86)

   def test_updateAltitude(self):
      self.assertAlmostEqual(updateAltitude(250, 10.5, 5.2), 263.1)
      self.assertAlmostEqual(updateAltitude(1000, 50, 20), 1060)
      self.assertAlmostEqual(updateAltitude(32.8, 13.9, 23.3), 58.35)

   def test_updateVelocity(self):
      self.assertAlmostEqual(updateVelocity(23.6, 83.2), 106.8)
      self.assertAlmostEqual(updateVelocity(14.7, 12.6), 27.3)
      self.assertAlmostEqual(updateVelocity(65.3, 91.9), 157.2)

   def test_updateFuel(self):
      self.assertAlmostEqual(updateFuel(265.3, 75.2), 190.1)
      self.assertAlmostEqual(updateFuel(42.1, 59.7), -17.6)
      self.assertAlmostEqual(updateFuel(635.89, 549.03), 86.86)

#Run the unit tests.
if __name__ == '__main__':
   unittest.main()

