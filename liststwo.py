"""
Other functions of lists
"""

numbers = [9, 23, 12, 10, 6, 11]

for index in range(len(numbers)):
    numbers[index] = numbers[index] * 2
print(numbers)

for v in zip(numbers):
    print(*v)


