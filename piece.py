from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class Piece(Widget):
    position_row = NumericProperty(-1)
    position_col = NumericProperty(-1)
    white = NumericProperty(1)
    visible = NumericProperty(1)
    p_size = NumericProperty(0)
    first = True
    offset_x = NumericProperty(-1)
    offset_y = NumericProperty(-1)

    def set(self, row, col):
        self.position_col = col
        self.position_row = row

    def set(self, pos):
        self.position_col = pos%8
        self.position_row = pos//8

class Knight(Piece):
    pass
class Bishop(Piece):
    pass
class Rook(Piece):
    pass
class Queen(Piece):
    pass
class King(Piece):
    pass
class Pawn(Piece):
    pass
