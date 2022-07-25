"""
Other functions of lists
"""

numbers = [9, 23, 12, 10, 6, 11]

for index in range(len(numbers)):
    numbers[index] = numbers[index] * 2
print(numbers)

for v in zip(numbers):
    print(*v)

"""
Sentence length
"""
sentence = input("Enter a sentence:")
words = sentence.split()
count = len(words)
if count > 20:
    print("Sentence is long. Type a shorter sentence")
else:
    print("There are", count, "words")



"""Append"""
myNumbers = []
for count in range(5):
    userNumber = int(input("Enter a number"))
    myNumbers.append(userNumber)
print(myNumbers)

