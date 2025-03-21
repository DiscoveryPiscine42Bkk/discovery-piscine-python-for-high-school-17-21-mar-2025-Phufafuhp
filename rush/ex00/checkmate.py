#!/bin/python3

def checkmate(board):
    if type(board) != str:
        return print("Err: Are you fucking with me?")

    #Turns the string into a two-dimensional array
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

    #Checks if there's a board *at all*
    if not chess_map[0]:
        return print("Err: Where's the board? You didn't give me shit!")
    
    #Checks if the board is a square
    if len(chess_map) != squares/len(chess_map):
        return print("Err: How did you fuck up a square? This is pre-school geometry!")

    #Searches for the king
    king_counter = 0
    y_index = 0
    for y in chess_map:
        x_index = 0
        for x in y:
            if x == "K":
                y_position = y_index
                x_position = x_index
                king_counter += 1
            x_index += 1
        y_index += 1
    
    #Checks if there's only one king
    if king_counter > 1:
        return print("Err: You're giving me more than I can work with, bud. Chill it with the kings.")
    elif king_counter == 0:
        return print("Err: Did you commit regicide? Where the hell is the king?")
    
    #Searches for pawns
    # print("Searching for pawns...")
    if y_position < len(chess_map)-1: 
        if x_position + 1 < len(chess_map):
            if chess_map[y_position+1][x_position+1] == "P":
                return print("Success")
        if x_position - 1 >= 0:
            if chess_map[y_position+1][x_position-1] == "P":
                return print("Success") 
    
    #Searches upward
    # print("Searching upward...")
    for i in chess_map[y_position::-1]:
        if i[x_position] in ["P","B"]:
            break
        elif i[x_position] in ["Q", "R"]:
            return print("Success")
        
    #Searches downward
    # print("Searching downward...")
    for i in chess_map[y_position:]:
        if i[x_position] in ["P", "B"]:
            break
        elif i[x_position] in ["Q", "R"]:
            return print("Success")
        
    # Searches left
    # print("Searching left...")
    for i in chess_map[y_position][x_position::-1]:
        if i in ["P", "B"]:
            break
        elif i in ["Q", "R"]:
            return print("Success")
        
    #Searches right
    # print("Searching right...")
    for i in chess_map[y_position][x_position:]:
        if i in ["P", "B"]:
            break
        elif i in ["Q", "R"]:
            return print("Success")
        
    #Searches up-left
    # print("Searching up-left...")
    x_left = x_position
    for i in chess_map[y_position::-1]:
        if x_left < 0 or i[x_left] in ["P", "R"]:
            break
        elif i[x_left] in ["Q", "B"]:
            return print("Success")
        x_left -= 1

    #Searches up-right
    # print("Searching up-right...")
    x_right = x_position
    for i in chess_map[y_position::-1]:
        if  x_right == len(chess_map) or i[x_right] in ["P", "R"]:
            break
        elif i[x_right] in ["Q", "B"]:
            return print("Success")
        x_right +=1

    #Searches down-left
    # print("Searching down-left...")
    x_left = x_position
    for i in chess_map[y_position:]:
        if x_left < 0 or i[x_left] in ["P", "R"]:
            break
        elif i[x_left] in ["Q", "B"]:
            return print("Success")
        x_left -= 1

    #Searches down-right
    # print("Searching down-right...")
    x_right = x_position
    for i in chess_map[y_position:]:
        if x_right == len(chess_map) or i[x_right] in ["P", "R"]:
            break
        elif i[x_right] in ["Q", "B"]:
            return print("Success")
        x_right += 1

    print("Failure")
    