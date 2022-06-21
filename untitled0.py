# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 09:21:06 2022

@author: bnzivu
"""

total = 0
count = 0
data = int(input("Enter a score or just return to quit: "))
while data != "":
    total += int(data)
    count += 1
    data = input("Enter a score or just return to quit: ")
if count <= 99:
    print("No of scores is", count)
else:
    print("No of scores", count)

