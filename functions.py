"""
Introduction to functions
"""
# Multiplies two numbers
def multiply (n, m):
    return n * m

a = 5
b = 6
c = multiply(a, b)

print(c)

# Performs arithmetic expressions on the value n
x = int(input("Enter a number [1 - 100] :"))
def dosomething (n):
    n = n * 2
    n = n ** 3
    n = n/5
    return n

if x < 1 or x >  100:
    print("Enter a number between 1 - 100")
else:
   print(dosomething(x))

# Encryter
def noVowels (message):
    vowels = "aeiou"
    secret = ""
    for letter in message:
        if not letter in vowels:
            secret = secret + letter
    return secret

your_message = input("Enter message: ")
print("Your secret message is", noVowels(your_message))

# Changes two letters to uppercase
def changeCase(s):
    new_s = ""
    for letter in s:
        if letter.islower():
            new_s = new_s + letter.upper()
        else:
            new_s = new_s + letter.lower()
    return new_s

message = "One Two"
print(changeCase(message))

# Runs repeatedly until the user enters a valid interger.
def getValidInterger (prompt, lower, upper):
    while True:
        number = int(input(prompt))
        if number < lower or number > upper:
            print("Error the number must range from" + str(lower) + "through" + str(upper))
        else:
            return number
