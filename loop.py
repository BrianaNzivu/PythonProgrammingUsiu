# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

total = 0
count = 0
while True:
    data = input("Enter a score or return to quit:")
    if data == "" :
        break
    total = total+ int(data)
    count = count + 1
    
if count == 0:
    print("The avaerage is 0")
else: 
    print("The avaerage is", total/count)
    
    