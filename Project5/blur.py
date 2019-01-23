#Project 5 - Image
#Names: Haley Childress and Ajay Patel
#Instructor: S. Einakian
#Section: 1

import math
import sys

args = sys.argv


def blur():
    try:
       if len(args) < 2:
          print('Usage: python blur.py <image> <OPTIONAL: reach>')

       if len(args) == 2:
          reach = 4
   
       else:
          reach = int(args[2])

       filename = args[1]

       fin = open(filename, 'r')
       finout = open('blur.ppm', 'w')
       
       pixellist = []
       pixelslist = []
       rowlist = []
       header = []
       linenum = 1
       col = 0
       row = 0
       width = 0
       height = 0

       for line in fin:
           line = line.strip()
           if linenum <= 3:
              header.append(line)

              if linenum == 2:
                 width = int(line.split(" ")[0])
                 height = int(line.split(" ")[1])
           
           if linenum == 3:
              fileformat(header, finout)
  
           if linenum > 3:
              pixellist.append(int(line)) 
              if len(pixellist) == 3:
                 rowlist.append(pixellist)
                 if col == width - 1:
                    pixelslist.append(rowlist)
                    rowlist = []
                    row += 1
                    col = 0
                 else:
                    col += 1  
  
                 pixellist = []
 
           linenum += 1

       updatepixels(pixelslist, finout, reach)
       finout.close()
       fin.close()


    except:
       print('Unable to open ' + filename)




def fileformat(header, finout):
    for value in header:
        finout.write('{:s}\n'.format(str(value)))


def group3list(lst):
    lst = [int(elements) for elements in lst]
    group3list = []
    for index in range(0, len(lst), 3):
        group3list.append(lst[index:index + 3])
    return group3list


def neighbor(currentpixel, colx, rowy, pixels, reach):
    neighborpixels = []

    xmin = colx - reach
    xmax = colx + reach 
    ymin = rowy - reach
    ymax = rowy + reach 
     
    if xmin < 0:
       xmin = 0
    else:
       xmin = xmin

    if xmax > len(pixels[0]):
       xmax = len(pixels[0])
    else:
       xmax = xmax

    if ymin < 0:
       ymin = 0
    else:
       ymin = ymin
  
    if ymax > len(pixels):
       ymax = len(pixels)
    else:
       ymax = ymax

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            if x == colx and y == rowy:
               pass
            else:
               neighborpixels.append(pixels[y][x])
    
    return neighborpixels


def avgofneighbor(currentpixel, colx, rowy, pixels, reach):
    pixelsofneighbors = neighbor(currentpixel, colx, rowy, pixels, reach)
    
    redcomsum = 0
    greencomsum = 0
    bluecomsum = 0
    totalpixels = len(pixelsofneighbors) + 1 
    
    for i in range(len(pixelsofneighbors)):
        redcomsum += pixelsofneighbors[i][0]
        greencomsum += pixelsofneighbors[i][1]
        bluecomsum += pixelsofneighbors[i][2]

    redcomsum += currentpixel[0]
    greencomsum += currentpixel[1]
    bluecomsum += currentpixel[2]

    redavg = redcomsum / totalpixels
    greenavg = greencomsum / totalpixels
    blueavg = bluecomsum / totalpixels

    pixelofavgs = [int(redavg), int(greenavg), int(blueavg)]
    return pixelofavgs


def writenewpixels(redcom, greencom, bluecom, finout):
    finout.write('{:s}\n'.format(str(redcom)))
    finout.write('{:s}\n'.format(str(greencom)))
    finout.write('{:s}\n'.format(str(bluecom)))


def updatepixels(pixels, finout, reach):
    for y in range(len(pixels)):
        for x in range(len(pixels[0])):
            currentpixel = pixels[y][x]
            colx = x
            rowy = y
            newpixel = avgofneighbor(currentpixel, colx, rowy, pixels, reach)
            redcom = newpixel[0]
            greencom = newpixel[1]
            bluecom = newpixel[2]
            writenewpixels(redcom, greencom, bluecom, finout)




if __name__ == '__main__':
   blur() 











