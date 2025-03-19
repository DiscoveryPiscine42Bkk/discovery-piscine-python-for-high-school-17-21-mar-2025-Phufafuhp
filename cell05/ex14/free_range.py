#!/usr/bin/env python3

import sys


if len(sys.argv) == 3:
    direction = 1 if sys.argv[1] < sys.argv[2] else -1
    array = [i for i in range(int(sys.argv[1]), int(sys.argv[2])+direction, direction)]
    print(array)
else:
    print("none")