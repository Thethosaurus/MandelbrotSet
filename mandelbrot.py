
from PIL import Image, ImageDraw
import random
import math
import PIL.Image
# from mpmath import *
RMAX = 2.0
RMIN = -2.0
IMAX = 2.0
IMIN = -2.0
LENGTH = 1000
WIDTH = 1000
a = .5
b = .5
pixel = complex(a, b)
img = Image.new("RGB", (WIDTH, LENGTH))
draw = ImageDraw.Draw(img)


def c_for_position(row, col):
   rPart = RMIN + ((RMAX - RMIN)/WIDTH)*col
   iPart = IMIN + ((IMAX - IMIN)/LENGTH)*row
   return complex(rPart,iPart)


def intoAnEquation():
   maxIteration = int(raw_input("How many iterations do you want to execute? "))
   pixelLoad = img.load()
   for row in range(LENGTH):
       for col in range(WIDTH):
           c = c_for_position(row, col)
           z = complex(0,0)
           for iteration in range(1, maxIteration):
               z = z**2 + c
               if abs(z) > 2:
                   redvalue = 255/iteration**2
                   greenvalue = 255/iteration*2
                   bluevalue = 255/iteration
                   img.putpixel((col, row), (redvalue, greenvalue, bluevalue))
                   break
               
   img.show()

intoAnEquation()
