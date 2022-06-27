
"""
Assignment on Strings
Author: Nzivu Briana
"""

myString = input("What is your statement")
#Prints string ten times
for i in range (10):
    print(myString)

#Prints length of String
noWords = len(myString)
print(noWords)

#Prints first character of the String
firstWord = myString[0]
print(firstWord)

#Prints first three characters of the string
print(myString[0:3])

#Prints last three characters of a string
print(myString[-3::])

#Prints last String backwards
print(myString[::-1])

#The seventh character of the string if the string is long enough and a message otherwise
if len(myString) >= 7:
    print(myString[6])
else:
    print("String has less than seven characters")

# The string with its first and last characters removed
print(myString[1:-1])

# The string in all caps
print(myString.upper())

# The string with every a replaced with an e
print(myString.replace("e", "a"))