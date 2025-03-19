#!/usr/bin/env python3

def array_of_names(dictarg):
    return [f"{x} {y}".title() for x, y in dictarg.items()]

persons = {
    "jean" : "valjean",
    "grace" : "hopper",
    "xavier" : "niel",
    "fifi" : "brindacier",
}

print(array_of_names(persons))
