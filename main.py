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

    def on_touch_down(self, touch):
        gui_board = backend.board()
        gui_board.reset_board()
        test = piece.Knight(p_size=self.p_size,offset_x=self.pos[0],offset_y=self.pos[1])
        self.add_widget(test)
        test.set(2,2)
        print("hit")

    def sync(self,board):
        test = Knight(p_size=self.p_size)
        self.add_widget(self)
        test.set(2,2)

if __name__ == '__main__':
    ChessApp().run()

