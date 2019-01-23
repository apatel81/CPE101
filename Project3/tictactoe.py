
#Project 3 - Tic-Tac-Toe Simulator
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1

from tictactoeFuncs import *
import random 

def main():
  
   Welcome()
   num = int(input("Do you wish to play against a (1) computer, or with (2)Players? "))
   while num < 1 or num > 2:
      print("ERROR: You must either play against (1) computer, or with (2)Players")
      num = int(input("Do you wish to play against (1) computer, or with (2)Players? ")) 

   if num == 1:
      board = createBoard()
      list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      print("  " + list[0] + " | " + list[1] + "  | " + list[2])
      print("------------")
      print("  " + list[3] + " | " + list[4] + "  | " + list[5])
      print("------------")
      print("  " + list[6] + " | " + list[7] + "  | " + list[8])

      letter = pickLetter()
      
      if letter == "X":
         print("")
         printBoard(board)
     
  
         cnt = 0
         while cnt < 9:
           if cnt%2 == 0:
              print("")
              print("It's Player 1's (X's) turn!")
              letter = "X"
              getInput(letter, board)
              print("")
              printBoard(board)
              rows = checkRows(board)
              cols = checkCols(board)
              diags = checkDiags(board)
              checkWin(rows, cols, diags)
              if checkWin(rows, cols, diags) == True:
                 break
              cnt += 1
           elif cnt%2 != 0:
              print("")
              print("It's Player 2's (O's) turn!")
              letter = 'O'
              spot = random.randint(1,9)
              if spot >= 1 and spot <= 9:
                 while board[spot-1] != "":
                    spot = random.randint(1,9)
                 board[spot-1] = letter                 
              print("")
              printBoard(board)
              rows = checkRows(board)
              cols = checkCols(board)
              diags = checkDiags(board)
              checkWin(rows, cols, diags)
              if checkWin(rows, cols, diags) == True:
                 break
              cnt += 1

         if cnt == 9:
            boardFull(board)
            if boardFull(board) == True:
               print("")
               print("Draw! The board is filled.")


      elif letter == "O":
         print("")
         printBoard(board)

         cnt = 0
         while cnt < 9:
           if cnt%2 == 0:
              print("")
              print("It's Player 1's (X's) turn!")
              letter = "X"
              spot = random.randint(1,9)
              if spot >= 1 and spot <= 9:
                 while board[spot-1] != "":
                    spot = random.randint(1,9)
                 board[spot-1] = letter
              print("")
              printBoard(board)
              rows = checkRows(board)
              cols = checkCols(board)
              diags = checkDiags(board)
              checkWin(rows, cols, diags)
              if checkWin(rows, cols, diags) == True:
                 break
              cnt += 1
           elif cnt%2 != 0:
              print("")
              print("It's Player 2's (O's) turn!")
              letter = 'O'
              getInput(letter, board)
              print("")
              printBoard(board)
              rows = checkRows(board)
              cols = checkCols(board)
              diags = checkDiags(board)
              checkWin(rows, cols, diags)
              if checkWin(rows, cols, diags) == True:
                 break
              cnt += 1

         if cnt == 9:
            boardFull(board)
            if boardFull(board) == True:
               print("")
               print("Draw! The board is filled.")


   elif num == 2:
      board = createBoard()
      list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
      print("  " + list[0] + " | " + list[1] + "  | " + list[2])
      print("------------")
      print("  " + list[3] + " | " + list[4] + "  | " + list[5])
      print("------------")
      print("  " + list[6] + " | " + list[7] + "  | " + list[8])

      letter = pickLetter() 
      print("")
      printBoard(board)   


      cnt = 0
      while cnt < 9:
        if cnt%2 == 0:
           print("")
           print("It's Player 1's (X's) turn!")
           letter = "X"
           getInput(letter, board)
           print("")
           printBoard(board)
           rows = checkRows(board)
           cols = checkCols(board)
           diags = checkDiags(board)
           checkWin(rows, cols, diags)
           if checkWin(rows, cols, diags) == True:
              break        
           cnt += 1
        elif cnt%2 != 0: 
           print("")
           print("It's Player 2's (O's) turn!")
           letter = 'O'
           getInput(letter, board)
           print("")
           printBoard(board)
           rows = checkRows(board)
           cols = checkCols(board)
           diags = checkDiags(board)
           checkWin(rows, cols, diags)
           if checkWin(rows, cols, diags) == True:
              break         
           cnt += 1
           
      if cnt == 9:
         boardFull(board)
         if boardFull(board) == True:
            print("")
            print("Draw! The board is filled.") 





if __name__ == '__main__':
   main()

 
