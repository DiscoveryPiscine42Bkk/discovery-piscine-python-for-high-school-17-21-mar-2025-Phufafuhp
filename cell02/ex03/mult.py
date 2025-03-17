#!/usr/bin/env python3

print("Enter the first number:")
first_number = float(input())
print("Enter the second number:")
second_number = float(input())
result = first_number*second_number
print("The result is negative.") if result < 0 else print("The result is positive.") if result > 0 else print("The result is negative and positive.")