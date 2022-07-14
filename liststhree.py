# """
# Increments in lists
# """
#
# numbers = [5, 9, 12, 1, 8]
# print(numbers)
#
# # index based for loop to process list
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] + 1
# print(numbers)
#
# # item based for loop to process list
# for items in numbers:
#     items = items * 2
#
# print(numbers)
# print()
#
# """
# Splitting in lists
# """
# s = "Python is cool"
# lst = s.split()
# print(lst)

"""
Pattern matching
"""
fileName = input("Enter the file name:")
inputFile = open(fileName, "r")
highGrade = 0
topStudent = "Nobody"

for line in inputFile:
    name, grade = line.split()
    grade = int(grade)
    if grade > highGrade:
        highGrade = grade
        topStudent = name
print(topStudent, "has a grade of", highGrade)