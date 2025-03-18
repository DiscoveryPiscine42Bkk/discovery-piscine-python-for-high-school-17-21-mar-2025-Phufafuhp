#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 1:
    print("parameters:",len(sys.argv)-1)
    for i in range(1,len(sys.argv)):
        print(sys.argv[i],":", len(re.findall("\w", sys.argv[i])))
else:
    print("none")

