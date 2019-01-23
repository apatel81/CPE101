#Lab 5
#Name: Ajay Patel
#Section: 1


def square_all(list):
    #To square the values in the original list and return the new list
    #list ---> list
    listsquared = []
    for i in range(len(list)):
        listsquared.append(list[i]**2)
    return listsquared

def add_n_all(list, n):
    #To create a new list that is the sum of the original list and n
    #list int ---> list
    newlist =[]
    i = 0 
    while i in range(len(list)):
         newlist.append(list[i] + n)
         i += 1    
    return newlist

def even_or_odd_all(list):
    #To create a function that determines if the elements of a list are even integers
    #list ---> true/false
    newlist = list
    newlist = [list[i] %2 == 0 for i in range(len(list))] 
    return newlist
