#!/usr/bin/env python3

import sys
def downcase_it(arg):
    return str(arg).lower()

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        print(downcase_it(i))
else:
    print("none")