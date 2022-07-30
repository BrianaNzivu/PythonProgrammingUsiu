"""
Author: Nzivu Briana M.
ID: 665436
A program that takes input from a text file and stores it in a dictionary.
"""
# Calculating total
def calculateTotal (d):
    total = 0
    for key in d:
        total = total + d[key]
    return total

# Opening file from folder
myFile = open('shopping.txt', 'r')
shopping = {}

# Storing file elements to dictonary
with open("shopping.txt") as f:
    for line in f:
        (item, value) = line.split()
        shopping[item] = int(value)


print('The toal shopping cost is', calculateTotal(shopping))

