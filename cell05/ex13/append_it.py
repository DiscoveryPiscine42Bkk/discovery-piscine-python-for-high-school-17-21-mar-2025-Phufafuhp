#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        if not sys.argv[i].endswith("ism"):
            print(sys.argv[i]+"ism")
else:
    print("none")