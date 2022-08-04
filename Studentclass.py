'''
Practice on Classes and objects for finals
'''

class Student:

    def __int__(self, name, age):
        self._name = name
        self._age = age

    def getAge (self):
        return self._age