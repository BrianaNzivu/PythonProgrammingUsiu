'''
Author : Briana Nzivu
ID: 665436
The following code is supposed to convert kilograms to pounds as many times as the user wants. It should then print out the list of pounds.
'''

n = int(input("How many data do you have"))
pound_list = []
for count in range (n):
    kilos = float(input('Enter the numberof kilograms:'))
    pounds = kilos * 2.2
    pound_list.append(pounds)

print('The pounds are', pound_list)