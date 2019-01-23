# Project 4 - Word Puzzle
# 
# Name: Haley Childress and  Ajay Patel
# Instructor: S. Einakian
# Section: 1

def getpuzzle(puzzle, words):
    #Input 100 character string and return 10x10 board
    #None --> list
    print("Puzzle:")
    print("") 
    print(puzzle[0:10])     
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:100])
    print('')

def checkforward(puzzle, word):
    #To check each row and see if any of the words is in the row 
    #list list ---> str
    found = False
    for row in range(10):
       start = row * 10
       end = start + 10
       if word in puzzle[start:end]:
          col = puzzle.index(word)
          print(word + ':' + ' (FORWARD)' + ' row: ' + str(row) + ' column: ' + str(col%10))
          found = True
       row += 1
    return found
   
def checkbackward(puzzle, word):
    #To check each row for the words backwards
    #list list ---> str
    found = False
    for row in range(10):
       start = row * 10
       end = start + 10   
       if word[::-1] in puzzle[start:end]:
             col = (puzzle.index(word[::-1])) + len(word) - 1
             print(word + ':' + ' (BACKWARD)' + ' row: ' + str(row) + ' column: ' + str(col%10))
             found = True
       row += 1
    return found

def checkdown(puzzle, word):
    #To check for words in the puzzle down
    #list list ---> str 
    found = False
    for col in range(10):
        if word in puzzle[col:100:10]:
           row = puzzle[col:100:10].index(word)
           print(word + ':' + ' (DOWN)' + ' row: ' + str(row) + ' column: ' + str(col))
           found = True
        col += 1
    return found

def checkup(puzzle, word):
    #To check for words the puzzle up
    #list list ---> str
    found = False
    for col in range(10):
        if word[::-1] in puzzle[col:100:10]:
           row = (puzzle[col:100:10].index(word[::-1])) + len(word) - 1
           print(word + ':' + ' (UP)' + ' row: ' + str(row) + ' column: ' + str(col))
           found = True
        col += 1
    return found

def notinpuzzle(forward, backward, up, down):
    if forward:
       return True
    elif backward:
       return True
    elif up:
       return True
    elif down:
       return True
    else:
       return False
