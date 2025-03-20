#!/bin/python3

from checkmate import checkmate

def main():
    board = """\
...k.
.....
RB...
.R...
....P\
"""
    checkmate(board)
    
if __name__ == "__main__":
    main()