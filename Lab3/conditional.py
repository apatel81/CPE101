#Lab3
#Name: Ajay Patel
#Section: 1

def max_101(a,b):
   #Compare which of two integers is greater
   #int int -> which is greater
   if a>b:
      #print(int(a))
      return a
   elif a<b:
      #print(int(b))
      return b
   else:
      return a==b
      #print(equal) 
 
def max_of_three(a,b,c):
    #Compare which of three floats is greatest
    #float float float -> which is greatest
    if a>b>c:
      #print(float(a))
      return a
    elif a>c>b:
      #print(float(a))
      return a
    elif b>c>a:
      #print(float(b))
      return b
    elif b>a>c:
      #print(float(b))
      return b
    elif c>b>a:
      #print(float(a))
      return c
    elif c>a>b:
      #print(float(c))
      return c
    else:
      return 0


def rental_late_fee(days):
     #Take the number of days late and return an int
     #int -> int
     if days<=0:
       #print(int(0))
       return 0
     elif days>0 and days<=9:
       #print(int(5))
       return 5
     elif days>9 and days<=15:
       #print(int(7))
       return 7
     elif days>15 and days<=24:
       #print(int(19))
       return 19  
     else:
       #print(int(100))       
       return 100
