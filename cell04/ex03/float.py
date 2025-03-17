#!/usr/bin/env python3

num = float(input("Give me a number: "))
if num != int(num):
    print("This number is a decimal.")
else:
    print("This number is an integer.")