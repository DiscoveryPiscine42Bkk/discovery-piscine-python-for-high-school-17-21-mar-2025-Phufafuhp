#!/usr/bin/env python3

print("Enter a number")
number = int(input())
multipler = 0

while multipler < 10:
    print(f'{multipler} x {number} = {multipler*number}')
    multipler += 1