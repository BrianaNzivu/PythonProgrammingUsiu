"""
Area of a circle
"""
from math import *

radius = input("What is the radius of your circle?")

if radius[0] == "-" and radius[1:].isnumeric():
    print("Error: Enter a number >= 0")

elif not radius.isnumeric():
    print("Enter a number not a letter")

else:
    radius = int(radius)
    area = pi * radius ** 2
print("Area of the circle is", area)
