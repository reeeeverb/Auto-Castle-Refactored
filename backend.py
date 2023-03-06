import presets

class board():
    color_arr = ["EMPTY"]*64
    piece_arr = ["EMPTY"]*64

    def reset_board(self):
        self.set_board(new_board_w)

    def set_board(self,loc,col):
        self.color_arr = col
        self.piece_arr = loc
