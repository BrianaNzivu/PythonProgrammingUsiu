"""
Introduction to functions
"""
def multiply (n, m):
    return n * m

a = 5
b = 6
c = multiply(a, b)

print(c)

x = int(input("Enter a number [1 - 100] :"))
def dosomething (n):
    n = n * 2
    n = n ** 3
    n = n/5
    return n

if x < 1 or x >  100:
    print("Enter a number between 1 - 100")
else:
   print(dosomething(x))
