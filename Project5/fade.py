#Project 5
#Name: Haley Childress and Ajay Patel
#Instructor: S. Einakian
#Section: 1

import math
import sys

args = sys.argv

def fade():
  filename = args[1]
  if len(args) == 5:
   try:
      fin = open(filename, 'r')
      finout = open('faded.ppm', 'w')


      linenum = 1
      pixel = []
      header = []
      colx = 0
      rowy = 0

      for line in fin:
         line = line.strip()
         if linenum <= 3:
            header.append(line)
            if linenum == 2:
               width = int(line.split(' ')[0])
               height = int(line.split(' ')[1])

         if linenum == 3:
            fileformat(header, finout)

         if linenum > 3:

             if len(group3list(line.split(' '))) >= 2:
                pixels = group3list(line.split(' '))
                for values in pixels:
                    if len(pixels) == 3:
                       singlepixel(values, colx, rowy, finout)
                       if colx == width - 1:
                          rowy += 1
                          colx = 0
                       else:
                          colx += 1
                pixel = []

             else:
                pixel.append(line)
                if len(pixel) == 3:
                   singlepixel(pixel, colx, rowy, finout)
                   if colx ==  width - 1:
                      rowy += 1
                      colx = 0
                   else:
                      colx += 1
                   pixel = []

         linenum += 1


      fin.close()
      finout.close()

   except:
      print('Unable to open ' + filename)
  else:
    print('Usage: python fade.py <image> <row> <column> <radius>')


def stringtointlist(lst):
    for elements in lst:
        for index in range(len(elements)):
            elements[index] = int(elements[index])
    return lst

def group3list(values):
    group3list = []
    for index in range(0, len(values), 3):
        group3list.append(values[index:index+3])
    group3list = stringtointlist(group3list)
    return group3list

def distance(pixel, givenpoint):
    return math.sqrt((pixel[0] - givenpoint[0]) ** 2 + (pixel[1] - givenpoint[1]) ** 2)

def scaledpixels(pixel, dist):
    radius = int(sys.argv[4])
    scale = (radius - dist) / radius
    if scale < 0.2:
       scale = 0.2
    else:
       scale = scale
    redcom = int(pixel[0])
    greencom = int(pixel[1])
    bluecom = int(pixel[2])
    pixel[0] = int(redcom * scale)
    pixel[1] = int(greencom * scale)
    pixel[2] = int(bluecom * scale)
    return pixel

def singlepixel(pixel, colx, rowy, finout):
    dist = distance((colx, rowy), (int(args[2]), int(args[3])))
    pixel =  scaledpixels(pixel, dist)
    redcom = pixel[0]
    greencom = pixel[1]
    bluecom = pixel[2]
    writenewpixels(redcom, greencom, bluecom, finout)

def fileformat(header, finout):
    for value in header:
        finout.write('{:s}\n'.format(str(value)))

def writenewpixels(redcom, greencom, bluecom, finout):
    finout.write('{:s}\n'.format(str(redcom)))
    finout.write('{:s}\n'.format(str(greencom)))
    finout.write('{:s}\n'.format(str(bluecom)))

if __name__ == '__main__':
   fade()

