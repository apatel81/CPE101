#Lab 5
#Name: Ajay Patel
#Section 1

import unittest
import poly

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)


   def test_poly(self):
     poly1 = [2.3, 4.7, 1.0]
     poly2 = [1.2, 2.1, -3.2]
     poly3 = poly.poly_add2(poly1, poly2) 
  
     poly4 = [1, 2, 3]
     poly5 = [4, 5, 6]
     poly6 = poly.poly_add2(poly4, poly5)
     
     poly7 = poly.poly_mult2(poly1, poly2)  
     poly8 = poly.poly_mult2(poly4, poly5)
  
     self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])
     self.assertListAlmostEqual(poly6, [5, 7, 9])
     self.assertListAlmostEqual(poly7, [2.76, 10.47, 3.71, -12.94, -3.2])
     self.assertListAlmostEqual(poly8, [4, 13, 28, 27, 18])   

if __name__ == '__main__':
   unittest.main()

