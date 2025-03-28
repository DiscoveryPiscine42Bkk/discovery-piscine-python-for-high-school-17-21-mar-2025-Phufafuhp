#!/bin/python3

def check(chess_map, king_y_index, king_x_index, color):
    from pieces import piece_dict
    #Searches for pawns
    # print("Searching for pawns...")
    

    if color == "white":
        if king_y_index - 1 >= 0: 
            if king_x_index + 1 < len(chess_map):
                if chess_map[king_y_index-1][king_x_index+1] == "p":
                    return 1
            if king_x_index - 1 >= 0:
                if chess_map[king_y_index-1][king_x_index-1] == "p":
                    return 1
    if color == "black":
        if king_y_index + 1 < len(chess_map):
            if king_x_index + 1 < len(chess_map):
                if chess_map[king_y_index+1][king_x_index+1] == "P":
                    return 1
            if king_x_index - 1 >= 0:
                if chess_map[king_y_index+1][king_x_index-1] == "P":
                    return 1
    # if king_y_index < len(chess_map)-1: 
    #     if king_x_index + 1 < len(chess_map):
    #         if chess_map[king_y_index+1][king_x_index+1] == "P":
    #             return 1
    #     if king_x_index - 1 >= 0:
    #         if chess_map[king_y_index+1][king_x_index-1] == "P":
    #             return 1 
    
    #Searches for knights
    if king_y_index >= 2:
        if king_x_index + 1 < len(chess_map):
            if chess_map[king_y_index-2][king_x_index+1] in ["N","n"] and piece_dict[chess_map[king_y_index-2][king_x_index+1]]["color"] != color:
                return 1
        if king_x_index >= 1:
            if chess_map[king_y_index-2][king_x_index-1] in ["N","n"] and piece_dict[chess_map[king_y_index-2][king_x_index-1]]["color"] != color:
                return 1
    
    if king_y_index + 2 < len(chess_map):
        if king_x_index + 1 < len(chess_map):
            if chess_map[king_y_index+2][king_x_index+1] in ["N","n"] and piece_dict[chess_map[king_y_index+2][king_x_index+1]]["color"] != color:
                return 1
        if king_x_index >= 1:
            if chess_map[king_y_index+2][king_x_index-1] in ["N","n"] and piece_dict[chess_map[king_y_index-2][king_x_index-1]]["color"] != color:
                return 1
    
    if king_x_index >= 2:
        if king_y_index + 1 < len(chess_map):
            if chess_map[king_y_index+1][king_x_index-2] in ["N","n"] and piece_dict[chess_map[king_y_index+1][king_x_index-2]]["color"] != color:
                return 1
        if king_y_index >= 1:
            if chess_map[king_y_index-1][king_x_index-2] in ["N","n"] and piece_dict[chess_map[king_y_index-1][king_x_index-2]]["color"] != color:
                return 1
            
    if king_x_index + 2 < len(chess_map):
        if king_y_index + 1 < len(chess_map):
            if chess_map[king_y_index+1][king_x_index+2] in ["N","n"] and piece_dict[chess_map[king_y_index+1][king_x_index+2]]["color"] != color:
                return 1
        if king_y_index >= 1:
            if chess_map[king_y_index-1][king_x_index+2] in ["N","n"] and piece_dict[chess_map[king_y_index-1][king_x_index+2]]["color"] != color:
                return 1
            
    #Searches for kings
    #Up of the king
    if king_y_index > 0:
        if chess_map[king_y_index-1][king_x_index] in ["K","k"] and piece_dict[chess_map[king_y_index-1][king_x_index]]["color"] != color:
            return 1
        if king_x_index - 1 > 0:
            if chess_map[king_y_index-1][king_x_index-1] in ["K","k"] and piece_dict[chess_map[king_y_index-1][king_x_index-1]]["color"] != color:
                return 1
        if king_x_index + 1 < len(chess_map):
            if chess_map[king_y_index-1][king_x_index+1] in ["K","k"] and piece_dict[chess_map[king_y_index-1][king_x_index+1]]["color"] != color:
                return 1
        
        #left and right
    if king_x_index > 0:
        if chess_map[king_y_index][king_x_index-1] in ["K", "k"] and piece_dict[chess_map[king_y_index][king_x_index-1]]["color"] != color:
            return 1
    if king_x_index + 1 < len(chess_map):
        if chess_map[king_y_index][king_x_index+1] in ["K", "k"] and piece_dict[chess_map[king_y_index][king_x_index+1]]["color"] != color:
            return 1
    
    #down of the king
    if king_y_index + 1 < len(chess_map):
        if chess_map[king_y_index+1][king_x_index] in ["K","k"] and piece_dict[chess_map[king_y_index+1][king_x_index]]["color"] != color:
            return 1
        if king_x_index >= 1:
            if chess_map[king_y_index+1][king_x_index-1] in ["K","k"] and piece_dict[chess_map[king_y_index+1][king_x_index-1]]["color"] != color:
                return 1
            if chess_map[king_y_index+1][king_x_index+1] in ["K","k"] and piece_dict[chess_map[king_y_index+1][king_x_index+1]]["color"] != color:
                return 1


    #Searches upward
    # print("Searching upward...")
    for i in chess_map[king_y_index::-1]:
        if i[king_x_index] in ["N", "n", "P", "p","B", "b"]:
            break
        elif i[king_x_index] in ["Q", "q", "R", "r"] and piece_dict[i[king_x_index]]["color"] != color:
            return 1
        
    #Searches downward
    # print("Searching downward...")
    for i in chess_map[king_y_index:]:
        if i[king_x_index] in ["N", "n", "P", "p","B", "b"]:
            break
        elif i[king_x_index] in ["Q", "q", "R", "r"] and piece_dict[i[king_x_index]]["color"] != color:
            return 1
        
    # Searches left
    # print("Searching left...")
    for i in chess_map[king_y_index][king_x_index::-1]:
        if i in ["N", "n", "P", "p","B", "b"]:
            break
        elif i in ["Q", "q", "R", "r"] and piece_dict[i]["color"] != color:
            return 1
        
    #Searches right
    # print("Searching right...")
    for i in chess_map[king_y_index][king_x_index:]:
        if i in ["N", "n", "P", "p","B", "b"]:
            break
        elif i in ["Q", "q", "R", "r"] and piece_dict[i]["color"] != color:
            return 1
        
    #Searches up-left
    # print("Searching up-left...")
    x_left = king_x_index
    for i in chess_map[king_y_index::-1]:
        if x_left < 0 or i[x_left] in ["P", "p", "R", "r", "N", "n"]:
            break
        elif i[x_left] in ["Q", "q", "B", "b"] and piece_dict[i[x_left]]["color"] != color:
            return 1
        x_left -= 1

    #Searches up-right
    # print("Searching up-right...")
    x_right = king_x_index
    for i in chess_map[king_y_index::-1]:
        if  x_right == len(chess_map) or i[x_right] in ["P", "p", "R", "r", "N", "n"]:
            break
        elif i[x_right] in ["Q", "q", "B", "b"] and piece_dict[i[x_right]]["color"] != color:
            return 1
        x_right +=1

    #Searches down-left
    # print("Searching down-left...")
    x_left = king_x_index
    for i in chess_map[king_y_index:]:
        if x_left < 0 or i[x_left] in ["P", "p", "R", "r", "N", "n"]:
            break
        elif i[x_left] in ["Q", "q", "B", "b"] and piece_dict[i[x_left]]["color"] != color:
            return 1
        x_left -= 1

    #Searches down-right
    # print("Searching down-right...")
    x_right = king_x_index
    for i in chess_map[king_y_index:]:
        if x_right == len(chess_map) or i[x_right] in ["P", "p", "R", "r", "N", "n"]:
            break
        elif i[x_right] in ["Q", "q", "B", "b"] and piece_dict[i[x_right]]["color"] != color:
            return 1
        x_right += 1

    return 0
    


# DELETE THIS LATER
# def display_array_board():
#     if array_board(board) != -1:
#         for x in array_board(board):
#             print(x)
#     else:
#         print("Error! Invalid chess board!")
    
# def find_enemy_piece(arr):
#     pass

# def find_king(arr):
    
#     if king_counter == 1:
#         #Search upward
#         for i in range(0,len(chess_row)):
#             pass
#         return king_y_index, king_x_index     
#     else: 
#         return -1

# def pawn_moves(position):
#     print(f"I work and my position in the array is [{position[0]}][{position[1]}]")

# seperator = "\n---------------------------------------------------------------------------------\n"

# checkmate(board)
# print(seperator)
# display_array_board()
# print(seperator)
# print(find_king(array_board(board)))
# find_enemy_piece(array_board(board))
# pawn_moves(find_king(array_board(board)))