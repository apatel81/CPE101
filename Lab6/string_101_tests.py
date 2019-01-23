#Lab 6
#Name: Ajay Patel
#Section 1

import unittest
import string_101

class TestCases(unittest.TestCase):

    def test_str_rot_13(self):
        self.assertEqual(string_101.str_rot_13('Hello'), 'Uryyb')
        self.assertEqual(string_101.str_rot_13('Clguba'), 'Python')

    def test_str_translate_101(self):
        self.assertEqual(string_101.str_translate_101('Hello', 'l', 'a'), 'Heaao')
        self.assertEqual(string_101.str_translate_101('Pythen', 'e', 'o'), 'Python')  

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

