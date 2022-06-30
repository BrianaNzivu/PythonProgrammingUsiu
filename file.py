filename = input("Enter a file name: ")
myfile = open(filename, "r")

wordcount  = 0

for line in myfile:
    wordcount += len(line.split())

print("The word count is", wordcount)