#Lab 7
#Name: Ajay Patel
#Section: 1

def groups_of_3(L):
    newlist = []
    i = 0
    while i < (len(L)):
        value = L[i:i+3]
        i += 3
        newlist.append(value)
    return newlist
