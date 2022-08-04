'''
Author : Briana Nzivu
ID: 665436
The following code adds to a dictonary the courses being taught by a lecturer.
'''

def workload (d):
    totalStudents= 0
    for noStudents in d:
        totalStudents = totalStudents + courses[noStudents]
    return totalStudents

courses = {}
for course in range(3):
    course = input('Enter course:')
    noStudents = int(input('Enter the number of students:'))
    courses[course] = noStudents

print('The total number of students is', workload(courses))