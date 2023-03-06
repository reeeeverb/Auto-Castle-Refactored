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

class ChessGame(Widget):
    s_width = NumericProperty(Window.width)
    s_height = NumericProperty(Window.height)
    pass

class ChessApp(App):
    def build(self):
        return ChessGame()

class Chessboard(Widget):
    gui_board = backend.board()
    gui_board.reset_board()

if __name__ == '__main__':
    ChessApp().run()

