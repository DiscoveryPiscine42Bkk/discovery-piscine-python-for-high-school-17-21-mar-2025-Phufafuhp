#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    # appearances = sys.argv[2].split().count(sys.argv[1]) 
    # print(appearances) if appearances > 0 else print("none")
    appearances = re.findall(sys.argv[1], sys.argv[2])
    print(len(appearances)) if len(appearances) > 0 else print("none")
else:
    print("none")