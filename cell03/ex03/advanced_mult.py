#!/usr/bin/env python3

table = 0
multipler = 0

while table < 11:
    print(f'Table de {table}: ',end="")
    while multipler < 11:
        print(f'{multipler*table}',end = " ")
        multipler += 1
    print("")
    multipler = 0
    table += 1