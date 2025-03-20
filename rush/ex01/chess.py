#!/bin/python3

board = """\
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR"""

#Turns number into (lowercase) letter trust me I will need this
letter = lambda x:chr(96+x)
#Turns (lowercase) letter into number
number = lambda x:ord(x)-96
#Turns the board into a two-dimensional array
    # I COULD just make the array, but I ain't typing allat

columns = ['a','b','c','d','e','f','g','h']
rows = [ str(x) for x in range(1,9)]
print(rows)
chess_map = []
chess_row = []
squares = 0
for square in board+('\n'):
    # if square not in ['\n','.','K','Q','P','R','B']:
    #     return print("Hey, asshole, give me something I can interpret, would you?")
    if square != '\n':
        chess_row.append(square)
        squares += 1
    else:
        chess_map.append(chess_row)
        chess_row = []

def select_square(square):
    print("I am functioning")
    print(f'square[0] = {square[0]}')
    print([x for x in "abcdefgh"])
    print(square[0] in [x for x in "abcdefgh"])
    print(f'square[1] = {square[1]}')
    print(square[1] in range(1,9))
    if (square[0] in columns) and (square[1] in rows):
        print("Valid Chess Square!")
    else:
        print("Invalid Chess Square!")

counter = 0
for x in chess_map:
    counter += 1
    print(x, counter)
for x in columns:
    print(f"  {x}  ", end = "")
print()

square = input("Enter a square : ")
select_square(square)