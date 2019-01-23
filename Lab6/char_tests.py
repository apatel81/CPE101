#Lab 6
#Name: Ajay Patel
#Section 1

import unittest
import char

class TestCases(unittest.TestCase):

    def test_is_lower_101(self):
        self.assertTrue(char.is_lower_101('b'), True)
        self.assertTrue(char.is_lower_101('z'), True)
        self.assertFalse(char.is_lower_101('A'), False)
   
    def test_char_rot13(self):
        self.assertEqual(char.char_rot13('a'), 'n')
        self.assertEqual(char.char_rot13('p'), 'c') 
        self.assertEqual(char.char_rot13('A'), 'N')
        self.assertFalse(char.char_rot13('/'), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()


