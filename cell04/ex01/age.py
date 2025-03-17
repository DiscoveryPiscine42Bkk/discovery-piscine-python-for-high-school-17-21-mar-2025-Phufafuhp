#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
prediction = 10
print(f"You are currently {age} years old.")
while prediction < 31:
    print(f"In {prediction} years, you'll be {age+prediction} years old.")
    prediction += 10
