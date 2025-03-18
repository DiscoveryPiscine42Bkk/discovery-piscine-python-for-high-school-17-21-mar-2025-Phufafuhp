#!/usr/bin/env python3

print("Enter a number")
number = int(input())
multipler = 0

for multiplier in range(10):
    print(f'{multiplier} x {number} = {multiplier*number}')