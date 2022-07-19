"""
Practice on dictonaries
"""
# To print specific key values
database = {'name':'Ken',
            'age':38,
            'gender': 'M',
            'occupation': 'Teacher'}

print(database['name'], 'is a',
      database['occupation'], 'and he is',
      database['age'], 'years old')

# To print the whole dictonary
for key in database:
    print(key, database[key])


# Using if method
if 'country' in database:
    print(database['name'],'comes from',
          database['country'])

# Using the get method
numbers = {'one': 1,
           'two': 2,
           'three': 3}
numbers.get('four', 'key missing')

# Creating a shopping one
shopping = {
    'apples': 300,
    'bread': 60,
    'bananas':100,
    'eggs': 360,
    'milk':110
}

total = 0
for key in shopping:
    total = total + shopping[key]

print("This shopping will cost Ksh", total)

# More advanced shopping one using a while loop
myShopping = {}
total = 0
while True:
    item = input('Enter an item:')
    if item == "":
        break
    price = float(input('Enter the price:'))
    myShopping[item] = price

for key in myShopping:
    print(key, myShopping[key])
    total = total + myShopping[key]

# More advanced shopping one using functions
def calculateTotal (d):
    total = 0
    for key in d:
        total = total + d[key]
    return total

print('Your shopping will cost', calculateTotal(myShopping))