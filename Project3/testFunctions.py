#Project 3 - Tic-Tact-Toe Simulator
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

import unittest
from tictactoeFuncs import *

class TestCases(unittest.TestCase):
   
   def test_checkRows(self):
       board1 = ['X','X','X','','','','','','']
       board2 = ['','','','','','','O','O','O']
       self.assertTrue(checkRows(board1), True)
       self.assertTrue(checkRows(board2), True)
   
   def test_checkCols(self):
       board3 = ['X','','','X','','','X','','']
       board4 = ['','O','','','O','','','O','']
       self.assertTrue(checkCols(board3), True)      
       self.assertTrue(checkCols(board4), True)
 
   def test_checkDiags(self):
       board5 = ['X','','','','X','','','','X']
       board6 = ['','','O','','O','','O','','']
       self.assertTrue(checkDiags(board5), True)
       self.assertTrue(checkDiags(board6), True)

   def test_boardFull(self):
       board7 = ['X','','','','','','','','']
       board8 = ['','','','','','','','','O']
       self.assertTrue(boardFull(board7), False)
       self.assertTrue(boardFull(board8), False)

   def test_checkWin(self):
       row1 = True
       col1 = False
       diag1 = False
       row2 = False
       self.assertTrue(checkWin(row1, col1, diag1), True)
       self.assertFalse(checkWin(row2, col1, diag1), False)

   def test_checkTurn(self):
       self.assertTrue(checkTurn(2), True)
       self.assertFalse(checkTurn(10), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

