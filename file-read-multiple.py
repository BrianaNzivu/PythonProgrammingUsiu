for i in range(3):
    fname = input("Enter file name: ")
    f = open(fname, "r")
    s = f.read()
    print(s.upper())
    f.close()