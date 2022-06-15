sideA = int(input("Enter the length of side A:"))
sideB = int(input("Enter the length of side B:"))
sideC = int(input("Enter the length of side C:"))
if sideA == sideB == sideC:
    print("This is an equilateral triangle")
elif sideA != sideC != sideB:
    print("This is an scalene")
elif sideA == sideB != sideC or sideB == sideC != sideA:
    print("This is an isoceless")