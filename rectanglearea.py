"""
Calculates the area of a rectangle
"""
def calculateArea (length, width):
    return length * width

def main ():
    length = int(input("Enter length:"))
    width = int(input("Enter width:"))
    print(calculateArea(length, width))

main()

