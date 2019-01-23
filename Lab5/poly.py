#Lab 5
#Name: Ajay Patel
#Section 1

def poly_add2(p1, p2):
    #This function takes 2 lists and adds them together to make 1 list
    #list list --> list
    sum = []
    sum.append(p1[0] + p2[0])
    sum.append(p1[1] + p2[1])
    sum.append(p1[2] + p2[2])
    return sum

def poly_mult2(p1, p2):
    #This function multiplies two lists/polynomials
    #list list ----> list
    sum = []
    sum.append(p1[0]*p2[0])
    sum.append((p1[1]*p2[0]) + (p1[0]*p2[1]))
    sum.append((p1[2]*p2[0]) + (p1[1]*p2[1]) + (p1[0]*p2[2]))
    sum.append((p1[2]*p2[1]) + (p1[1]*p2[2]))
    sum.append((p1[2]*p2[2]))
    return sum    
