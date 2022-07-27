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

# Counting four letter words
twoFile = open('lorem.txt', 'r')
wordCounter = 0
for line in twoFile:
 words = line.split()
for word in words:
 if len(word) == 4:
   wordCounter += 1
print(wordCounter)

#Averaging intergers from a file
threeFile = open('intergers.txt', 'r')
count = 0

for line in threeFile:
    line = int(line.strip())
    numbers = int(line)

    count += numbers
    average = count//line

print("The avaerage is", average)




