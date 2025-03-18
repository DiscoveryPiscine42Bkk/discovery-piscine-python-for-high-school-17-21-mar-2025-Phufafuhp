#!/usr/bin/env python3

def greetings(arg="noble stranger"):
    print(f"Hello, {arg}.") if isinstance(arg, str) else print("Error! It was not a name.")
        
greetings('Alexandra')
greetings('Will')
greetings()
greetings(42)