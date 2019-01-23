# Lab 4
#
# Name: Ajay Patel
# Instructor: Sussan Einakian
# Section: 1

import driver

def letter(row, col):
     if row<=col:
       return 'W' 
     else:
       return 'T'

if __name__ == '__main__':
        driver.comparePatterns(letter)


