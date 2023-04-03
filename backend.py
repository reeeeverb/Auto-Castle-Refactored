import copy
import math
from presets import *
import generate

class board():
    pgn = "" 
    color_arr = ["EMPTY"]*64
    piece_arr = ["EMPTY"]*64
    forward = "WHITE"
    current_move = "WHITE"
    w_en_passantable = None
    b_en_passantable = None
    w_en_passantable_s = None
    b_en_passantable_s = None
    w_queen_castle = True
    w_king_castle = True
    b_queen_castle = True
    b_king_castle = True
    w_king_location = None
    b_king_location = None
    winner = -1
    move = 0

    def reset_board(self):
        self.set_board(new_board_w_piece,new_board_w_color)
        self.queen_castle = True
        self.king_castle = True
        self.w_king_location = 3
        self.b_king_location = 59
        self.pgn = "" 

    def set_board(self,loc,col):
        self.color_arr = col
        self.piece_arr = loc

    def set_piece(self,square,piece,color):
        self.color_arr[square] = color
        self.piece_arr[square] = piece

    def clear_square(self,square):
        self.color_arr[square] = "EMPTY"
        self.piece_arr[square] = "EMPTY"
    
    def move_piece(self,down_square,up_square):
        pgn_castle = None
        t_color_arr = copy.copy(self.color_arr)
        t_piece_arr = copy.copy(self.piece_arr)
        t_forward = copy.copy(self.forward)
        t_current_move = copy.copy(self.current_move)
        t_w_en_passantable = copy.copy(self.w_en_passantable)
        t_b_en_passantable = copy.copy(self.b_en_passantable)
        t_w_en_passantable_s = copy.copy(self.w_en_passantable_s)
        t_b_en_passantable_s = copy.copy(self.b_en_passantable_s)
        t_w_queen_castle =  copy.copy(self.w_queen_castle)
        t_w_king_castle = copy.copy(self.w_king_castle)
        t_b_queen_castle = copy.copy(self.b_queen_castle)
        t_b_king_castle = copy.copy(self.b_king_castle)
        t_w_king_location = copy.copy(self.w_king_location)
        t_b_king_location = copy.copy(self.b_king_location)
            
        piece = self.piece_arr[down_square]
        if piece == "EMPTY":
            return;
        color = self.color_arr[down_square]
        if color != self.current_move:
            return;
        if up_square not in generate.moves(down_square,self):
            return
        t_w_en_passantable = self.w_en_passantable
        t_b_en_passantable = self.b_en_passantable
        t_w_en_passantable_s = self.w_en_passantable_s
        t_b_en_passantable_s = self.b_en_passantable_s
        self.w_en_passantable = None
        self.b_en_passantable = None
        promotion = False
        if piece == "KING":
            pgn_start = "K"
            if abs(up_square - down_square) == 2:
                sign = (down_square-up_square)//2
                new_s = up_square+sign
                if up_square < 3:
                    #KING SIDE CASTLE
                    pgn_castle = "O-O"
                    self.clear_square(up_square-sign)
                else:
                    #QUEEN SIDE CASTLE
                    pgn_castle = "O-O-O"
                    self.clear_square(up_square-(2*sign))
                self.set_piece(new_s,"ROOK",color)
            if color == "WHITE":
                self.w_king_location = up_square
                self.w_queen_castle = False
                self.w_king_castle = False
            elif color == "BLACK":
                self.b_king_location = up_square
                self.b_queen_castle = False
                self.b_king_castle = False
        elif piece == "ROOK":
            pgn_start = "R"
            if color == "WHITE":
                if down_square == 0 or down_square == 56:
                    self.w_king_castle = False
                elif down_square == 7 or down_square == 63:
                    self.w_queen_castle = False
            elif color == "BLACK":
                if down_square == 0 or down_square == 56:
                    self.b_king_castle = False
                elif down_square == 7 or down_square == 63:
                    self.b_queen_castle = False
        elif piece == "PAWN":
            pgn_start = ""
            if up_square - down_square == 16:
                if color == "WHITE":
                    self.w_en_passantable = down_square+8
                    self.w_en_passantable_s = up_square
                if color == "BLACK":
                    self.b_en_passantable = up_square+8
                    self.b_en_passantable_s = up_square
            elif down_square - up_square == 16:
                if color == "WHITE":
                    self.w_en_passantable = down_square-8
                    self.w_en_passantable_s = up_square
                if color == "BLACK":
                    self.b_en_passantable = up_square+8
                    self.b_en_passantable_s = up_square
            elif abs(up_square - down_square) != 8:
                if color == "WHITE" and up_square == t_b_en_passantable:
                    self.color_arr[t_b_en_passantable_s] = "EMPTY"
                    self.piece_arr[t_b_en_passantable_s] = "EMPTY"
                elif color == "BLACK" and up_square == t_w_en_passantable:
                    self.color_arr[t_w_en_passantable_s] = "EMPTY"
                    self.piece_arr[t_w_en_passantable_s] = "EMPTY"
            if up_square//8 == 0 or up_square//8 == 7:
                promotion = True
        elif piece == "KNIGHT":
            pgn_start = "N"
        else:
            pgn_start = piece[0]
        pgn_capture = "" if self.piece_arr[up_square] == "EMPTY" else "x"
        pgn_end = decode(up_square) + " "
        self.color_arr[down_square] = "EMPTY"
        self.piece_arr[down_square] = "EMPTY"
        self.color_arr[up_square] = color
        self.piece_arr[up_square] = piece
        if self.current_move == "WHITE":
            check_pos = generate.in_check(self.w_king_location,self) 
            if check_pos != -1:  
                self.color_arr = t_color_arr
                self.piece_arr = t_piece_arr
                self.forward = t_forward
                self.current_move = t_current_move
                self.w_en_passantable = t_w_en_passantable
                self.b_en_passantable = t_b_en_passantable
                self.w_en_passantable_s = t_w_en_passantable_s
                self.b_en_passantable_s = t_b_en_passantable_s
                self.w_queen_castle =  t_w_queen_castle
                self.w_king_castle = t_w_king_castle
                self.b_queen_castle = t_b_queen_castle
                self.b_king_castle = t_b_king_castle
                self.w_king_location = t_w_king_location
                self.b_king_location = t_b_king_location
            else:
                self.pgn += str(self.move//2+1) + ". "
                self.pgn += pgn_start+pgn_capture+pgn_end if pgn_castle == None else pgn_castle
                self.move += 1
                self.current_move = "BLACK"
                check_pos = generate.in_check(self.b_king_location,self) 
                if check_pos != -1 and generate.checkmate(self,check_pos,self.b_king_location,"BLACK"):
                    self.winner = "WHITE"
                if promotion:
                    return up_square
        elif self.current_move == "BLACK":
            check_pos = generate.in_check(self.b_king_location,self) 
            if check_pos != -1:
                self.color_arr = t_color_arr
                self.piece_arr = t_piece_arr
                self.forward = t_forward
                self.current_move = t_current_move
                self.w_en_passantable = t_w_en_passantable
                self.b_en_passantable = t_b_en_passantable
                self.w_en_passantable_s = t_w_en_passantable_s
                self.b_en_passantable_s = t_b_en_passantable_s
                self.w_queen_castle =  t_w_queen_castle
                self.w_king_castle = t_w_king_castle
                self.b_queen_castle = t_b_queen_castle
                self.b_king_castle = t_b_king_castle
                self.w_king_location = t_w_king_location
                self.b_king_location = t_b_king_location
            else:
                self.pgn += pgn_start+pgn_capture+pgn_end if pgn_castle == None else pgn_castle
                self.move += 1
                self.current_move = "WHITE"
                check_pos = generate.in_check(self.w_king_location,self) 
                if check_pos != -1 and generate.checkmate(self,check_pos,self.w_king_location,"WHITE"):
                    self.winner = "BLACK"
                if promotion:
                    return up_square

def decode(square):
    return str(chr(97+square//8))+ str(square%8)
