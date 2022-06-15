"""
This program identifies whether a triangle is a right angled triangles or not using if elif else statement and logic statements
"""
sideA = float(input("Enter the length of side A:"))
sideB = float(input("Enter the length of side B:"))
sideC = float(input("Enter the length of side C:"))

if sideB <= 0 or sideA <= 0 or sideC <= 0:
    print("Enter valid length")
elif sideA ** 2 + sideB ** 2 == sideC ** 2:
    print("Right angle")
else:
    print("Not right angled")