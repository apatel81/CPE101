#Project 6 - Crime Time
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 1



class Crime:
#Attributes: ID Number, Category, Day of Week, Month, Time(AM/PM)
   
   def __init__(self, ID, Category):
       self.ID = ID
       self.Category = Category
       self.Day = None
       self.Month = None
       self.Time = None

   def __repr__(self):
       return '{} {} {} {} {}'.format(self.ID, self.Category, self.Day, self.Month, self.Time)

   def __eq__(self, other):
       return (type(other) == Crime and self.ID == other.ID)

   def __set_time__(self, day_of_week, month, hour):
       self.Day = day_of_week

       monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
       self.Month = monthlist[month - 1]

       hour = str(hour)

       if hour == '0':
          hour = '12 AM'
       elif '1' <= hour <= '11':
          hour = hour + 'AM'
       elif hour == '12':
          hour == '12 PM'
       else:
          hour = str(int(hour) -12) + 'PM'

       self.Time = hour


def create_crimes(lines):
    #Take input and format into one line
    #str(s) ---> list
    rob_idlist = []
    for line in lines:
        input = line.split('\t')
        if str(input[1]) == 'ROBBERY':
           if input not in rob_idlist:
              rob_idlist.append(input)

    L = [Crime(int(x[0]), 'ROBBERY') for x in rob_idlist]
    return L
 
 
def sort_crimes(crimes):
    #selection sort
    #list -> list
    for i in range(len(crimes)):
        minIndex = i
        for k in range(i + 1, len(crimes)):
            if crimes[k].ID < crimes[minIndex].ID:
               minIndex = k   
        swap(crimes, minIndex, i )
    return crimes
   
  
def swap(A, x, y):
    #swap the value
    #list  int int ->   
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def update_crimes(crimes, lines):
    #To find the ID in times.tsv and then update Crime() with day, month, and time
    #list list ---> list
    for line in lines:
        input = line.split('\t')
        crime = find_crime(crimes, int(input[0]))
        ID = input[0]
        Category = 'ROBBERY'
        #input[1] = crimes[midpoint].Day 
        Day = input[1]
        Month = input[2]
        Time = input[3]
        print(ID, Category, Day, Month, Time)

        #update = set_time(Day, Month, Time)

    return (Crime(ID, Category))



def find_crime(crimes, crime_id):
    #Binary Serach on sorted list
    #list -> bool 
    first = 0
    last = len(crimes)-1
    found = False
    while first<=last and not found:
          midpoint = (first + last)//2
          if crimes[midpoint].ID == crime_id:
             found = True
             return Crime(crime_id, 'ROBBERY')
          else:
             if crime_id < crimes[midpoint].ID:
                last = midpoint-1
             else:
                first = midpoint+1

