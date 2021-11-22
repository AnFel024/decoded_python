import math

import os
import json
import string 
import PIL.Image as Image


for i in range(100): 
    print (str(i)+" : "+string.printable[i])

with open("img.png", "rb") as image:
    image = image.read()
    a_byte_array = bytearray(image)

print(a_byte_array)
