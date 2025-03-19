#!/usr/bin/env python3

array = [1, 4, 8, 6, 8, 42, 67, -9, 42]
print(array)
print(set([x + 2 for x in array if x > 5]))