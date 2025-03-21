#!/bin/python3
from pieces import piece_dict
from check import check

def chess(board):

    #Turns number into (lowercase) letter trust me I will need this
    letter = lambda x:chr(96+x)
    #Turns (lowercase) letter into number, specifically to reference indices
    number = lambda x:ord(x)-97
    # piece_list = [["K",'k'],["Q","q"],["R","r"],["B","b"],["N","n"],["P","p"]]
    # Turns the board into a two-dimensional array
        # I COULD just make the array, but I ain't typing allat
    columns = ['a','b','c','d','e','f','g','h']
    rows = [ str(x) for x in range(1,9)]
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

    def produce_valid_squares(chosen_piece, chosen_y_index, chosen_x_index):
        def king_squares(king, king_y_index, king_x_index):

            #THIS IS TOO DAMN LONG
            king_squares = []
            king_color = piece_dict[king]["color"]
            #Up of the king
            if king_y_index > 0:
                if piece_dict[chess_map[king_y_index-1][king_x_index]]["color"] != king_color:
                    king_squares.append((king_y_index-1, king_x_index))
                if king_x_index - 1 >= 0:
                    if piece_dict[chess_map[king_y_index-1][king_x_index-1]]["color"] != king_color:
                        king_squares.append((king_y_index-1,king_x_index-1))
                if king_x_index + 1 < len(chess_map):
                    if piece_dict[chess_map[king_y_index-1][king_x_index+1]]["color"] != king_color:
                        king_squares.append((king_y_index-1, king_x_index+1))
            
            #left and right
            if king_x_index > 0 and piece_dict[chess_map[king_y_index][king_x_index-1]]["color"] != king_color:
                king_squares.append((king_y_index,king_x_index-1))
            if king_x_index + 1 < len(chess_map) and piece_dict[chess_map[king_y_index][king_x_index+1]]["color"] != king_color:
                king_squares.append((king_y_index,king_x_index+1))
            
            #down of the king
            if king_y_index + 1 < len(chess_map):
                if piece_dict[chess_map[king_y_index+1][king_x_index]]["color"] != king_color:
                    king_squares.append((king_y_index+1, king_x_index))
                if king_x_index - 1 >= 0:
                    if piece_dict[chess_map[king_y_index+1][king_x_index-1]]["color"] != king_color:
                            king_squares.append((king_y_index+1,king_x_index-1))
                if king_x_index + 1 < len(chess_map):
                    if piece_dict[chess_map[king_y_index+1][king_x_index+1]]["color"] != king_color:
                            king_squares.append((king_y_index+1, king_x_index+1))
            return king_squares

        def rook_squares(rook, rook_y_index, rook_x_index):
            rook_squares = []
            rook_up_index = rook_y_index
            rook_down_index = rook_y_index
            rook_left_index = rook_x_index
            rook_right_index = rook_x_index

            #Valid squares upward
            for i in chess_map[rook_y_index::-1]:
                # print(i[rook_x_index] == ".")
                # print(piece_dict[i[rook_x_index]]["color"] != piece_dict[rook]["color"])
                # print(rook_up_index != rook_y_index)
                # print(f'rook_up_index =', rook_up_index)
                # print(f'rook_y_index =', rook_y_index)
                if i[rook_x_index] == ".":
                    rook_squares.append((rook_up_index, rook_x_index))
                elif piece_dict[i[rook_x_index]]["color"] != piece_dict[rook]["color"]:
                    rook_squares.append((rook_up_index, rook_x_index))
                    break
                # Checks ands stops if there's a piece that's the same color (and is not itself)
                elif piece_dict[i[rook_x_index]]["color"] == piece_dict[rook]["color"] and rook_up_index != rook_y_index:
                    break
                rook_up_index -= 1

            #Valid squares downward
            for i in chess_map[rook_y_index:]:
                if i[rook_x_index] == ".":
                    rook_squares.append((rook_down_index, rook_x_index))
                elif piece_dict[i[rook_x_index]]["color"] != piece_dict[rook]["color"]:
                    rook_squares.append((rook_down_index, rook_x_index))
                    break
                # Checks ands stops if there's a piece that's the same color (and is not itself)
                elif piece_dict[i[rook_x_index]]["color"] == piece_dict[rook]["color"] and rook_down_index != rook_y_index:
                    break
                rook_down_index += 1

            #Valid squares leftward
            for i in chess_map[rook_y_index][rook_x_index::-1]:
                if i == ".":
                    rook_squares.append((rook_y_index, rook_left_index))
                elif piece_dict[i]["color"] != piece_dict[rook]["color"]:
                    rook_squares.append((rook_y_index, rook_left_index))
                    break
                # Checks ands stops if there's a piece that's the same color (and is not itself)
                elif piece_dict[i]["color"] == piece_dict[rook]["color"] and rook_left_index != rook_x_index:
                    break
                rook_left_index -= 1
            
            #Valid squares rightward
            for i in chess_map[rook_y_index][rook_x_index:]:
                if i == ".":
                    rook_squares.append((rook_y_index, rook_right_index))
                elif piece_dict[i]["color"] != piece_dict[rook]["color"]:
                    rook_squares.append((rook_y_index, rook_right_index))
                    break
                # Checks ands stops if there's a piece that's the same color (and is not itself)
                elif piece_dict[i]["color"] == piece_dict[rook]["color"] and rook_right_index != rook_x_index:
                    break
                rook_right_index += 1
            
            return rook_squares

        def bishop_squares(bishop, bishop_y_index, bishop_x_index):
            bishop_squares = []
            
            bishop_up_index = bishop_y_index
            bishop_down_index = bishop_y_index
            bishop_left_index = bishop_x_index
            bishop_right_index = bishop_x_index
            bishop_color = piece_dict[bishop]["color"]

            #valid squares up-left
            for i in chess_map[bishop_y_index::-1]:
                if bishop_left_index < 0 or (piece_dict[i[bishop_left_index]]["color"] == bishop_color and bishop_up_index != bishop_y_index):
                    bishop_up_index = bishop_y_index
                    bishop_left_index = bishop_x_index
                    break
                if i[bishop_left_index] == ".":
                    bishop_squares.append((bishop_up_index, bishop_left_index))
                elif piece_dict[i[bishop_left_index]]["color"] != bishop_color:
                    bishop_squares.append((bishop_up_index, bishop_left_index))
                    bishop_up_index = bishop_y_index
                    bishop_left_index = bishop_x_index
                    break
                bishop_up_index -= 1
                bishop_left_index -= 1
            
            #valid squares up-right
            for i in chess_map[bishop_y_index::-1]:
                if bishop_right_index == len(chess_map) or (piece_dict[i[bishop_right_index]]["color"] == bishop_color and bishop_up_index != bishop_y_index):
                    bishop_up_index = bishop_y_index
                    bishop_right_index = bishop_x_index
                    break
                elif i[bishop_right_index] == ".":
                    bishop_squares.append((bishop_up_index, bishop_right_index))
                elif piece_dict[i[bishop_right_index]]["color"] != bishop_color:
                    bishop_squares.append((bishop_up_index, bishop_right_index))
                    bishop_up_index = bishop_y_index
                    bishop_right_index = bishop_x_index
                    break
                bishop_up_index -= 1
                bishop_right_index += 1

            #valid squares down-left
            for i in chess_map[bishop_y_index:]:
                if bishop_left_index < 0 or (piece_dict[i[bishop_left_index]]["color"] == bishop_color and bishop_down_index != bishop_y_index):
                    bishop_down_index = bishop_y_index
                    bishop_left_index = bishop_x_index
                    break
                elif i[bishop_left_index] == ".":
                    bishop_squares.append((bishop_down_index, bishop_left_index))
                elif piece_dict[i[bishop_left_index]]["color"] != bishop_color:
                    bishop_squares.append((bishop_down_index, bishop_left_index))
                    bishop_down_index = bishop_y_index
                    bishop_left_index = bishop_x_index
                    break
                bishop_down_index += 1
                bishop_left_index -= 1

            #valid squares down-right
            for i in chess_map[bishop_y_index:]:
                if bishop_right_index == len(chess_map) or (piece_dict[i[bishop_right_index]]["color"] == bishop_color and bishop_down_index != bishop_y_index):
                    bishop_down_index = bishop_y_index
                    bishop_right_index = bishop_x_index
                    break
                elif i[bishop_right_index] == ".":
                    bishop_squares.append((bishop_down_index, bishop_right_index))
                elif piece_dict[i[bishop_right_index]]["color"] != bishop_color:
                    bishop_squares.append((bishop_down_index, bishop_right_index))
                    bishop_down_index = bishop_y_index
                    bishop_right_index = bishop_x_index
                    break
                bishop_down_index += 1
                bishop_right_index += 1
            return bishop_squares

        def knight_squares(knight, knight_y_index, knight_x_index):
            knight_squares = []
            knight_color = piece_dict[knight]["color"]

            if knight_y_index >= 2:
                if knight_x_index + 1 < len(chess_map) and piece_dict[chess_map[knight_y_index-2][knight_x_index+1]]["color"] != knight_color:
                    knight_squares.append((knight_y_index - 2, knight_x_index + 1))
                if knight_x_index >= 1 and piece_dict[chess_map[knight_y_index-2][knight_x_index-1]]["color"] != knight_color:
                    knight_squares.append((knight_y_index - 2, knight_x_index - 1))
            
            if knight_y_index + 2 < len(chess_map):
                if knight_x_index + 1 < len(chess_map) and piece_dict[chess_map[knight_y_index+2][knight_x_index+1]]["color"] != knight_color:
                    knight_squares.append((knight_y_index + 2, knight_x_index + 1))
                if knight_x_index >= 1 and piece_dict[chess_map[knight_y_index-2][knight_x_index-1]]["color"] != knight_color:
                    knight_squares.append((knight_y_index + 2, knight_x_index - 1))
            
            if knight_x_index >= 2:
                if knight_y_index + 1 < len(chess_map) and piece_dict[chess_map[knight_y_index+1][knight_x_index-2]]["color"] != knight_color:
                    knight_squares.append((knight_y_index + 1, knight_x_index - 2))
                if knight_y_index >= 1 and piece_dict[chess_map[knight_y_index-1][knight_x_index-2]]["color"] != knight_color:
                    knight_squares.append((knight_y_index - 1, knight_x_index - 2))
            
            if knight_x_index + 2 < len(chess_map):
                if knight_y_index + 1 < len(chess_map) and piece_dict[chess_map[knight_y_index+1][knight_x_index+2]]["color"] != knight_color:
                    knight_squares.append((knight_y_index + 1, knight_x_index + 2))
                if knight_y_index >= 1 and piece_dict[chess_map[knight_y_index-1][knight_x_index+2]]["color"] != knight_color:
                    knight_squares.append((knight_y_index - 1, knight_x_index + 2))

            return knight_squares

        def pawn_squares(pawn, pawn_y_index, pawn_x_index):
            pawn_squares = []
            direction = piece_dict[pawn]["direction"]
            if pawn_y_index == piece_dict[pawn]["start_position"] and chess_map[pawn_y_index+(direction*2)][pawn_x_index] == ".":
                pawn_squares.append((pawn_y_index+(direction*2), pawn_x_index)) 
            if chess_map[pawn_y_index+(direction)][pawn_x_index] == ".":
                pawn_squares.append((pawn_y_index+direction, pawn_x_index)) 
            if pawn_x_index+1 != len(chess_map):
                if chess_map[pawn_y_index+(direction)][pawn_x_index+1] != "." and piece_dict[chess_map[pawn_y_index+direction][pawn_x_index+1]]["color"] != piece_dict[pawn]["color"]:
                    pawn_squares.append((pawn_y_index+direction, pawn_x_index+1))
            if pawn_x_index-1 >= 0:
                if chess_map[pawn_y_index+(direction)][pawn_x_index-1] != "." and piece_dict[chess_map[pawn_y_index+direction][pawn_x_index-1]]["color"] != piece_dict[pawn]["color"]:
                    pawn_squares.append((pawn_y_index+direction, pawn_x_index-1))
            return pawn_squares
            # if color == "white":
            #     if pawn_y_index == 6:
            #         pawn_squares.append((pawn_y_index-2,pawn_x_index))
            #     pawn_squares.append((pawn_y_index-1, pawn_x_index))
            # else:
            #     if pawn_y_index == 1:
            #         pawn_squares.append((pawn_y_index+2,pawn_x_index))
            #     pawn_squares.append((pawn_y_index+1, pawn_x_index))
            # return pawn_squares
            # pass

        if chosen_piece in ["K", "k"]:
            return king_squares(chosen_piece, chosen_y_index, chosen_x_index)
        elif chosen_piece in ["Q","q"]:
            return rook_squares(chosen_piece, chosen_y_index, chosen_x_index) + bishop_squares(chosen_piece, chosen_y_index, chosen_x_index)
        elif chosen_piece in ["R", "r"]:
            return rook_squares(chosen_piece, chosen_y_index, chosen_x_index)
        elif chosen_piece in ["B", "b"]:
            return bishop_squares(chosen_piece, chosen_y_index, chosen_x_index)
        elif chosen_piece in ["N", "n"]:
            return knight_squares(chosen_piece, chosen_y_index, chosen_x_index)
        elif chosen_piece in ["P", "p"]:
            return pawn_squares(chosen_piece, chosen_y_index, chosen_x_index)

    def find_k_index(chess_map, color):

        if color == "white":
            king = "K"
        else:
            king = "k"
        
        y_index = 0
        for y in chess_map:
            x_index = 0
            for x in y:
                if x == king:
                    king_y_index = y_index
                    king_x_index = x_index
                x_index += 1
            y_index += 1
        
        return (king_y_index, king_x_index)


    turn_counter = 1
    while True:
        for current_color in ["white", "black"]:
            print(f'Turn {turn_counter}, {current_color.capitalize()}')
            king_index = find_k_index(chess_map, current_color)
            if check(chess_map, king_index[0], king_index[1], current_color) == 1:
                print("King in check!")
            row_counter = 8
            for x in chess_map:
                print(x, row_counter)
                row_counter -= 1
            for x in columns:
                print(f"  {x}  ", end = "")
            print()
            while True:
                chosen_square = input("Choose a piece : ")     
                if len(chosen_square) == 2 and (chosen_square[0] in columns) and (chosen_square[1] in rows):
                    chosen_y_index = len(chess_map)-int(chosen_square[1])
                    chosen_x_index = number(chosen_square[0])
                    chosen_piece = chess_map[chosen_y_index][chosen_x_index]
                    if piece_dict[chosen_piece]["color"] == current_color:
                        valid_squares = produce_valid_squares(chosen_piece, chosen_y_index, chosen_x_index)
                        if valid_squares:
                            choosing_square = input(f'Where shall you move your {piece_dict[chosen_piece]["name"]}? : ')
                            if len(choosing_square) == 2 and (choosing_square[0] in columns) and (choosing_square[1] in rows):
                                choosing_y_index = len(chess_map)-int(choosing_square[1])
                                choosing_x_index = number(choosing_square[0])
                                if (choosing_y_index,choosing_x_index) in valid_squares:
                                    if chosen_piece in ["P", "p"] and choosing_y_index in [0,7]:
                                        if chosen_piece == "P":
                                            chess_map[choosing_y_index][choosing_x_index] = "Q"
                                        else:
                                            chess_map[choosing_y_index][choosing_x_index] = "q"
                                    elif chosen_piece in ["K", "k"]:
                                        chess_map[choosing_y_index][choosing_x_index] = chosen_piece
                                        chess_map[chosen_y_index][chosen_x_index] = "."
                                        if check(chess_map, choosing_y_index, choosing_x_index, current_color) == 1:
                                            print("You can't put your king in check!")
                                            continue
                                    chess_map[choosing_y_index][choosing_x_index] = chosen_piece
                                    chess_map[chosen_y_index][chosen_x_index] = "."
                                    king_index = find_k_index(chess_map, current_color)
                                    if check(chess_map, king_index[0], king_index[1], current_color) == 1:
                                        print("King still in check!")
                                    else:
                                        break
                                else:
                                    print("Invalid move")
                            else: 
                                print("Invalid square!")
                        else:
                            print("Piece is immovable!")
                    else:
                        print("Invalid piece!")
                else:
                    print("Invalid square!")
        turn_counter += 1