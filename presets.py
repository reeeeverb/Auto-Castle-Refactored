import math

new_board_w_piece = ["ROOK","KNIGHT","BISHOP","QUEEN","KING","BISHOP","KNIGHT","ROOK",\
                    "PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN",\
                    "ROOK","KNIGHT","BISHOP","KING","QUEEN","BISHOP","KNIGHT","ROOK"]

new_board_b_piece = ["ROOK","KNIGHT","BISHOP","KING","QUEEN","BISHOP","KNIGHT","ROOK",\
                    "PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                    "PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN","PAWN",\
                    "ROOK","KNIGHT","BISHOP","QUEEN","KING","BISHOP","KNIGHT","ROOK"]
                   
new_board_w_color = ["WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE",\
                     "WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK",\
                     "BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK"]

new_board_b_color = ["BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK",\
                     "BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK","BLACK",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY","EMPTY",\
                     "WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE",\
                     "WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE","WHITE"]

def square_pos(x,y,width):
    square_size = width/8
    return (math.trunc(y/square_size),math.trunc(x/square_size),math.trunc(y/square_size)*8+math.trunc(x/square_size))
