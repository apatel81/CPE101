#Project 4 - Word Puzzle
#Name: Haley Childress and Ajay Patel
#Instructor: S. Einakian
#Section: 1

from funcs import*

def main():
    puzzle = input()
    words = input().split()     
    getpuzzle(puzzle, words)   
    for word in words:    
        forward = checkforward(puzzle, word)
        backward = checkbackward(puzzle, word)
        down = checkdown(puzzle, word)
        up = checkup(puzzle, word)

        notinpuzzle(forward, backward, down, up)
        if notinpuzzle(forward, backward, down, up) == False:
           print(word + ':' + ' word not found')           

if __name__ == '__main__':
   main()
