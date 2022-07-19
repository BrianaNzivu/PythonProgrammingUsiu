"""
Practice on dictonaries
"""
database = {'name':'Ken',
            'age':38,
            'gender': 'M',
            'occupation': 'Teacher'}

print(database['name'], 'is a',
      database['occupation'], 'and he is',
      database['age'], 'years old')

if 'country' in database:
    print(database['name'],'comes from',
          database['country'])