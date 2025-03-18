#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 1:
    print("parameters:",len(sys.argv)-1)
    for i in sys.argv[1:]:
        print(i,":", len(re.findall("\w", i)))
else:
    print("none")

