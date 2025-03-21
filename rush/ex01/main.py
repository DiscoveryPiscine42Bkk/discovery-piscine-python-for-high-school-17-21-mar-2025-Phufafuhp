#!/bin/python3
from chess import chess

def main():
    board = """\
rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBKQBNR\
"""
    chess(board)
    
if __name__ == "__main__":
    main()