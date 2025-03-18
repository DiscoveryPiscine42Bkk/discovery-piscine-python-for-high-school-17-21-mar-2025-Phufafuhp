#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    z = sys.argv[1].count("z")
    print("z"*z) if z > 0 else print("none")
    # for x in sys.argv[1]:
    #     if x == "z": print(x,end = "")
    # print("\n")
else:
    print("none")
    