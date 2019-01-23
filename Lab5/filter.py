#Lab 5
#Name: Ajay Patel 
#Section 1

def are_positive(list):
    #Create a function that returns a list of postive integers from an existing list
    #list ----> list
    poslist = []
    for i in range(len(list)):
        if list[i] > 0:
           poslist.append(list[i])
    return poslist

def are_greater_than_n(list, n):
    #Create a function that when given a list, returns a list with values greater than n
    #list ----> list
    greaterlist = []
    i = 0
    while i < len(list): 
        if list[i] > n:
          greaterlist.append(list[i]) 
        i += 1  
    return greaterlist


def are_dividable_by_n(list, n):
    #Create a function that gives a list of integers dividable by n 
    #list ----> list
    divlist = [list[i] for i in range(len(list)) if list[i] %n == 0]    
    return divlist
