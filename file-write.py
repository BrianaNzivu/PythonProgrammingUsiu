filename = input("Enter file name: ")
myfile = open(filename, "w")
myfile.write("Two lines \n of text")
myfile.close()