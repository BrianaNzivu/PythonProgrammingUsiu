'''
Conntinuation on dictonaries
'''

months = {
    'Jan' : 31,
    'Feb' : 28,
    'Mar' : 31,
    'Apr' : 30,
    'May' : 31,
    'Jun' : 30,
    'Jul' : 31,
    'Aug' : 31,
    'Sep' : 30,
    'Oct' : 31,
    'Nov' : 30,
    'Dec' : 31,
}

mon = input("Enter your fave month")
month_list = list(months.keys())
month_list.sort()
mon = mon.title()
print(month_list)
print(mon, 'has', months[mon], 'days')

# Adding a key
days = {
    'Mon': 1,
    'Tue' : 2,
    'Wed' : 3,
    'Thur': 4,
    'Sat': 6,
    'Sun': 7,
}

days['Fri'] = 5
days.pop('Fri')
