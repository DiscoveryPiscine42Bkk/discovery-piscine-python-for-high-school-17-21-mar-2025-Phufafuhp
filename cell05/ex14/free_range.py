#!/usr/bin/env python3

import sys

array =[]
print(sys.argv)
if len(sys.argv) == 3:
    if sys.argv[1] < sys.argv[2]:
        for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
            array.append(i)
    else:
        for i in range(int(sys.argv[1]), int(sys.argv[2])-1, -1):
            array.append(i)
    print(array)
else:
    print("none")