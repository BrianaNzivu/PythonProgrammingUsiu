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