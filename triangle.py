"""
This program identifies whether a triangle is quilateral, scalene or isosceles
"""

sideA = int(input("Enter the length of side A:"))
sideB = int(input("Enter the length of side B:"))
sideC = int(input("Enter the length of side C:"))
if sideA == sideB == sideC:
    print("This is an equilateral triangle")
elif sideA != sideC != sideB:
    print("This is an scalene")
else:
    print("This is an isosceles")