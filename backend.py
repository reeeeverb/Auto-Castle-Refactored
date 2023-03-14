import math
from presets import *
import generate

class board():
    color_arr = ["EMPTY"]*64
    piece_arr = ["EMPTY"]*64
    forward = "WHITE"
    current_move = "WHITE"
    w_en_passantable = None
    b_en_passantable = None
    w_queen_castle = True
    w_king_castle = True
    b_queen_castle = True
    b_king_castle = True
    move = 0

    def reset_board(self):
        self.set_board(new_board_w_piece,new_board_w_color)
        self.queen_castle = True
        self.king_castle = True

    def set_board(self,loc,col):
        self.color_arr = col
        self.piece_arr = loc
    
    def move_piece(self,down_square,up_square):
        piece = self.piece_arr[down_square]
        if piece == "NOTHING":
            return;
        color = self.color_arr[down_square]
        if color != self.current_move:
            return;
        if up_square not in generate.moves(down_square,self):
            return
        w_en_passantable = None
        b_en_passantable = None
        if piece == "KING":
            if color == "WHITE":
                w_queen_castle = False
                w_king_castle = False
            elif color == "BLACK":
                b_queen_castle = False
                b_king_castle = False
        elif piece == "ROOK":
            if color == "WHITE":
                if down_square == 0 or down_square == 56:
                    w_king_castle = False
                elif down_square == 7 or down_square == 63:
                    w_queen_castle = False
            elif color == "BLACK":
                if down_square == 0 or down_square == 56:
                    b_king_castle = False
                elif down_square == 7 or down_square == 63:
                    b_queen_castle = False
        elif piece == "PAWN":
            if up_square - down_square == 16:
                if color == "WHITE":
                    self.w_en_passantable = down_square+8
                if color == "BLACK":
                    self.b_en_passantable = up_square+8
            elif down_square - up_square == 16:
                if color == "WHITE":
                    self.w_en_passantable = down_square-8
                if color == "BLACK":
                    self.b_en_passantable = up_square-8
                
        self.color_arr[down_square] = "EMPTY"
        self.piece_arr[down_square] = "EMPTY"
        self.color_arr[up_square] = color
        self.piece_arr[up_square] = piece
        self.move += 1
        self.current_move = "WHITE" if color == "BLACK" else "BLACK"
