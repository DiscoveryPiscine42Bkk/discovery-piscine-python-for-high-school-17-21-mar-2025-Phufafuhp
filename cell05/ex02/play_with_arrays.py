#!/usr/bin/env python3

array = [1, 4, 6, 8, 67, -9, 42]
print(array)

i=0
while i < len(array):
    if array[i] > 5:
         array[i] += 2
    else:
         array.pop(i)
         i -=1
    i += 1 

print(array)