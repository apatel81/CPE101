# Project 3 - Tic-Tac-Toe Simulator
# 
# Name: Ajay Patel
# Instructor: S. Einakian 
# Section: 1
# Functions definitions comes here

  
def Welcome():
   #Display welcome message, rules, and ask user for how many players
   #str int ---> int
   print("Welcome to this Tic-Tac-Toe Simulator.")
   print("Your goal is to line up 3 of your tics in either a line or a diagonol.")
   print("You will pick either X or O. X will go first")
   #num = int(input("Do you wish to play against a (1) computer, or with (2)Players? "))     
   #while num < 1 or num > 2:
      #print("ERROR: You must either play against (1) computer, or with (2)Players")
      #num = int(input("Do you wish to play against (1) computer, or with (2)Players? "))
      #if num == 1:
         #return 1
      #elif num == 2:
         #return 2
 
def createBoard():
   #Create a function that creates a list for X and O
   #none ----> list
   board = ['','','','','','','','','']
    
   print("The board postions are as follows:")

   return board

def printBoard(board):
   #Display the empty board so users can play
   #none ----> none
   print("  " + board[0] + " | " + board[1] + "  | " + board[2])   
   print("------------")
   print("  " + board[3] + " | " + board[4] + "  | " + board[5])
   print("------------")
   print("  " + board[6] + " | " + board[7] + "  | " + board[8])
   
def pickLetter():
   #Create a function that asks user to pick X or O
   #int ----> str
   letter = str(input("Choose X or O: "))
   while not(letter == "X" or letter == "O"):
     print("ERROR: Invalid letter please use X or O")
     letter = str(input("Choose X or O: "))
   if letter == "X":
     return letter
   elif letter  == "O":
     return letter

def getInput(letter, board):
   #Ask user where they want to place letter
   #int ----> str (in spot that correlates with int)
   spot = int(input("Where do you like to place your letter (pick in range of 1-9): "))
   while spot < 1 or spot > 9:
      print("Invalid move! Location does not exist. Please try again.")
      spot = int(input("Where do you like to place your letter (pick in range of 1-9): "))   
   if spot >= 1 and spot <= 9:
      while board[spot-1] != "":
         print("Invalid move! Location is already taken. Please try again.")
         spot = int(input("Where do you like to place your letter (pick in range of 1-9): "))
      board[spot-1] = letter
      return board

def checkRows(board):
   #To check if there are any winning combinations in rows
   #board ----> true and letter if there is a winning combination
   if "X" in board[0] and "X" in board[1] and "X" in board[2]:
     print("")
     print("Winner is X!")
     return (True, "X")
   elif "X" in board[3] and "X" in board[4] and "X" in board[5]:
     print("")
     print("Winner is X!")
     return (True, "X")
   elif "X" in board[6] and "X" in board[7] and "X" in board[8]:
     print("")
     print("Winner is X!")
     return (True, "X")
   elif "O" in board[0] and "O" in board[1] and "O" in board[2]:
     print("")
     print("Winner is O!")
     return (True, "O")
   elif "O" in board[3] and "O" in board[4] and "O" in board[5]:
     print("")
     print("Winner is O!")
     return (True, "O")
   elif "O" in board[6] and "O" in board[7] and "O" in board[8]:
     print("")
     print("Winner is O!")
     return (True, "O")   
   else:
     return False

def checkCols(board):
   #to check if there are any winnig combinatiosn in columns
   #board -----> true and letter if there is a winning combination
   if "X" in board[0] and "X" in board[3] and "X" in board[6]:
      print("")
      print("Winner is X!")
      return (True, "X") 
   elif "X" in board[1] and "X" in board[4] and "X" in board[7]:
      print("")
      print("Winner is X!")
      return (True, "X")  
   elif "X" in board[2] and "X" in board[5] and "X" in board[8]:
      print("")
      print("Winner is X!") 
      return (True, "X")
   elif "O" in board[0] and "O" in board[3] and "O" in board[6]:
      print("")
      print("Winner is O!")
      return (True, "O")
   elif "O" in board[1] and "O" in board[4] and "O" in board[7]:
      print("")
      print("Winner is O!")
      return (True, "O")
   elif "O" in board[2] and "O" in board[5] and "O" in board[8]:
      print("")
      print("Winner is O!")
      return (True, "O")
   else:
      return False

def checkDiags(board):
   #To check ic there are any winning combinations in diagonols
   #board ---> true and letter if there is a winning combination
   if "X" in board[0] and "X" in board[4] and "X" in board[8]:
      print("")
      print("Winner is X!")
      return (True, "X") 
   elif "X" in board[2] and "X" in board[4] and "X" in board[6]:
      print("")
      print("Winner is X!")
      return (True, "X")
   elif "O" in board[0] and "O" in board[4] and "O" in board[8]:
      print("")
      print("Winner is O!")
      return (True, "O")
   elif "O" in board[2] and "O" in board[4] and "O" in board[6]:
      print("")
      print("Winner is O!")
      return (True, "O")
   else:
      return False
        
def boardFull(board):
    for i in range(len(board)):
        if board[i] == ' ':
           return False
    return True

def checkWin(rows, cols, diags):
     if rows:
        return True
     elif cols:
        return True
     elif diags:
        return True
     else:
        return False

def checkTurn(count):
   while count < 9:
     count += 1 
     return count
