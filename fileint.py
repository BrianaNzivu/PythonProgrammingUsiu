filename =  input("Enter a file name: ")
myfile = open(filename, "w")

for i in range (1, 11):
    myfile.write(str(i) + "")

myfile.write("\n The end")
myfile.close()
