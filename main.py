import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.lang.builder import Builder
import backend
import piece

class ChessGame(Widget):
    s_width = NumericProperty(Window.width)
    s_height = NumericProperty(Window.height)
    pass

class ChessApp(App):
    def build(self):
        return ChessGame()

class Chessboard(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.p_size = ObjectProperty(0)
        pos = ObjectProperty()
        Window.bind(on_resize=self.on_window_resize)
        self.current_board = None

    def on_window_resize(self, window, width, height):
        if self.current_board != None:
            self.sync(self.current_board)

    def add_piece(self,name,position):
        if name == "EMPTY":
            return
        elif name == "KNIGHT":
            temp = piece.Knight(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        elif name == "BISHOP":
            temp = piece.Bishop(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        elif name == "ROOK":
            temp = piece.Rook(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        elif name == "QUEEN":
            temp = piece.Queen(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        elif name == "KING":
            temp = piece.King(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        elif name == "PAWN":
            temp = piece.Pawn(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        self.add_widget(temp)
        temp.set(position)

    def on_touch_down(self, touch):
        gui_board = backend.board()
        gui_board.reset_board()
        self.sync(gui_board)

    def sync(self,board):
        self.current_board = board
        self.clear_widgets()
        for square, piece in enumerate(board.piece_arr):
            self.add_piece(piece,square)

if __name__ == '__main__':
    ChessApp().run()

