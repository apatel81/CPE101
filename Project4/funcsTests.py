#Project 4 - Word Puzzle
#Name: Haley Childress and Ajay Patel
#Instructor: S. Einakian
#Section: 1

import unittest
import funcs

class TestCases(unittest.TestCase):

   def test_checkforward(self):
       list1 = ('einhelloow'+
                'jflewnfjif'+
                'eaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaaacoolaa'+     
                'aaaaaaaaaa'+
                'aaaaaaaaaa')
       word1 = 'hello'
       word2 = 'cool'
       self.assertTrue(funcs.checkforward(list1, word1))
       self.assertTrue(funcs.checkforward(list1, word2))
   
   def test_checkbackward(self):
       list1 = ('einhelloow'+
                'jflewnfjif'+
                'eaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaatabaaaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa'+
                'aaaacoolaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa')
       word1 = 'bat'
       word2 = 'python'
       self.assertTrue(funcs.checkbackward(list1, word1))
       self.assertFalse(funcs.checkbackward(list1, word2))
 
   def test_checkdown(self):
       list1 = ('einhelloow'+
                'jflewnfjif'+
                'eaaaaaaaaa'+
                'aasaaalaaa'+
                'aataaaaaaa'+
                'aaoatabaaa'+
                'aapaaaaaaa'+
                'aaaacoolaa'+
                'aaaaaaaaaa'+
                'aaaaaaaaaa')  
       word1 = 'stop'
       word2 = 'lab'
       word3 = 'cool'
       self.assertTrue(funcs.checkdown(list1, word1))    
       self.assertTrue(funcs.checkdown(list1, word2))
       self.assertFalse(funcs.checkdown(list1, word3)) 

   def test_checkup(self):
       list1 = ('einhelloow'+
                'jflewnfjif'+
                'eaaaaalaaa'+
                'aasaaalaaa'+
                'aataaaaaaa'+
                'aaoatabaaa'+
                'aaptaaaaaa'+
                'aaascoolaa'+
                'aaaiaaaaaa'+
                'aaalaaaaaa')
       word1 = 'awesome'
       word2 = 'list'
       word3 = 'ball'
       self.assertFalse(funcs.checkup(list1, word1))
       self.assertTrue(funcs.checkup(list1, word2))
       self.assertTrue(funcs.checkup(list1, word3))

   def test_notinpuzzle(self):
       forward = False
       backward = False
       down = False
       up = False
       forward1 = True
       self.assertFalse(funcs.notinpuzzle(forward, backward, down, up))
       self.assertTrue(funcs.notinpuzzle(forward1, backward, down, up))
                   
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()



