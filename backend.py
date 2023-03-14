from presets import *
import generate

class board():
    color_arr = ["EMPTY"]*64
    piece_arr = ["EMPTY"]*64
    forward = "WHITE"
    current_move = "WHITE"
    move = 0

    def reset_board(self):
        self.set_board(new_board_w_piece,new_board_w_color)

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
        self.color_arr[down_square] = "EMPTY"
        self.piece_arr[down_square] = "EMPTY"
        self.color_arr[up_square] = color
        self.piece_arr[up_square] = piece
        self.move += 1
        self.current_move = "WHITE" if color == "BLACK" else "BLACK"
