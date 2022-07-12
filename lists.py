"""
Addition in lists
"""

a = [11, 21, 36]

#Way one
total = 0
for i in range(len(a)):
    total += a[i]

print("the total is", total)

#Way two
totalTwo = 0
for index in a:
    totalTwo = totalTwo + index
print("the total is", totalTwo)

#Way three
def add(x, y):
    return x + y

print("The total is", sum(a))

print(add(5, 9))
