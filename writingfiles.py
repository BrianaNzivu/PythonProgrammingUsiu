"""
Practice on files for finals
"""
# Writing to a file
myFile = open('random.txt', 'w')
myFile.write('Two line of code')

myFile.close()

# Writing intergers to a file
myFile = open('random.txt', 'w')

for i in range(1, 11):
    myFile.write(str(i) + '\n')
myFile.close()

# Checking is a file exists
import os

myFile = input('Enter file name:')
openFile = open(myFile, 'r')
if os.path.exists(myFile):
    openFile.read()
else:
    print('File does not exist')