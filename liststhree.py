"""
Increments in lists
"""

numbers = [5, 9, 12, 1, 8]
print(numbers)

# index based for loop to process list
for i in range(len(numbers)):
    numbers[i] = numbers[i] + 1
print(numbers)

# item based for loop to process list
for items in numbers:
    items = items * 2

print(numbers)
print()

