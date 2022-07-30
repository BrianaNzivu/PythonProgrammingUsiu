"""
Practice on functions for finals
"""
# Square root of a number
# def sqrt (n):
#     return n ** 2
# n = float(input("Enter number: "))
# print(sqrt(n))

# Checks if a number is even
def checkEven(x):
    return x % 2

x = float(input("Enter number: "))
divide = checkEven(x)

if divide > 0.0:
    print('Number is odd')
else:
    print('Number is even')