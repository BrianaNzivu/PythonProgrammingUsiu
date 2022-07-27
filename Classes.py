"""
Practicing classes
"""
class Person:
    def __init__(self, name, id_num, height):
        self._name = name
        self._id_num = id_num
        self._height = height

    def get_name(self):
        return self._name

    def get_id_num (self):
        return self._id_num

    def get_height (self):
        return self._height

    def set_height(self, height):
        self._height = height

    def __str__(self):
        return 'Name: ' + self._name + '\nHeight: ' + str(self._height)

p = Person('Jane', 12345, 3)
print('Name:', p.get_name())
print("Id Number:", p.get_id_num())