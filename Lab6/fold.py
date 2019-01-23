#Lab 6
#Name: Ajay Patel
#Section: 1

from functools import reduce

def sumfunction(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    return total

def index_of_smallest(L):
    x = 0

    if len(L) <= 0:
       return -1

    if len(L) > 0:
       for i in range(len(L)):
           if type(L[i]) == list:
              L[i] = reduce(lambda x,y : x if x < y else y, L[i])
           if type(L[i]) == list:
              L[i] = reduce(lambda x,y : x if x < y else y, L[x])
           if L[i] < L[x]:
              x = i 
       return x
