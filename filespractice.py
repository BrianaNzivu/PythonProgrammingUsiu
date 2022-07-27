"""
Practice on files for finals
"""
# Reading a file using for method
myFile = open("shopping.txt", 'r')

for line in myFile:
 line = myFile.read()
 print(line)

# Reading a file using while loop
myFile = open("shopping.txt", 'r')
while True:
 line = myFile.readline()
 if line == '':
  break
 print(line[:-1])

#Counting the number of words
myFile = open('shopping.txt', 'r')
wordCount = 0

for line in myFile:
 wordCount += len(line.split())
print(wordCount)