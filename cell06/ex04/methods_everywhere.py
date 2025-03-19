#!/usr/bin/env python3

import sys

def shrink(arg):
    print(arg[:8])

def enlarge(arg):
    print(arg+("Z"*(8-len(arg))))

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        shrink(i) if len(i) > 8 else enlarge(i) if len(i) < 8 else print(i)
else:
    print("none")