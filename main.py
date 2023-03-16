import math
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.button import Button
from kivy.lang.builder import Builder
import backend, presets, piece, generate

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
        self.down_square = None
        self.up_square = None
        self.marker_list = []
        enpassantable_move = [-1,-1]

    def on_window_resize(self, window, width, height):
        if self.current_board != None:
            self.sync(self.current_board)

    def show(self,square,board):
        for spot in generate.moves(square[2], board):
            self.add_marker(spot)

    def add_marker(self,spot):
        column = spot%8
        row = spot//8
        self.new_red = Image(source='chess-pieces/red-circle.png',pos=(self.x+self.p_size*column,self.y+self.p_size*row),size=(self.p_size,self.p_size))
        self.add_widget(self.new_red)
        self.marker_list.append(self.new_red)

    def add_piece(self,name,color,position):
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
        if color == "BLACK":
            temp.white = 0
        self.add_widget(temp)
        temp.set(position)

    def on_touch_down(self, touch):
        if self.children == []:
            gui_board = backend.board()
            gui_board.reset_board()
            self.sync(gui_board)
            return
        if not self.collide_point(*touch.pos):
            return
        xpos = touch.pos[0]-self.pos[0]
        ypos = touch.pos[1]-self.pos[1]
        self.down_square = (presets.square_pos(xpos,ypos,self.width))
        if self.down_square != self.up_square:
            for widget in self.marker_list:
                self.remove_widget(widget)

    def on_touch_up(self,touch):
        if not self.collide_point(*touch.pos):
            return
        xpos = touch.pos[0]-self.pos[0]
        ypos = touch.pos[1]-self.pos[1]
        self.up_square = (presets.square_pos(xpos,ypos,self.width))
        if self.up_square == self.down_square:
            self.show(self.up_square,self.current_board)
        elif self.up_square != None and self.down_square != None:
            promote_square = self.current_board.move_piece(self.down_square[2],self.up_square[2])
            self.sync(self.current_board)
            if promote_square != None:
                content = BoxLayout(orientation = 'vertical')
                embedded_content = BoxLayout(orientation = 'horizontal')
                embedded_content1 = BoxLayout(orientation = 'horizontal')
                image1 = Image(source='chess-pieces/white/knight1.png')
                image2 = Image(source='chess-pieces/white/bishop1.png')
                image3 = Image(source='chess-pieces/white/rook1.png')
                image4 = Image(source='chess-pieces/white/queen1.png')
                embedded_content.add_widget(image1)
                embedded_content.add_widget(image2)
                content.orientation = "vertical"
                embedded_content1.add_widget(image3)
                embedded_content1.add_widget(image4)
                content.add_widget(embedded_content)
                content.add_widget(embedded_content1)
                popup = Popup(title = "Promotion",content=content,
                        size_hint=(None, None), size=(200, 200))
                popup.open()
                print("promotion detected")

    def sync(self,board):
        self.current_board = board
        self.clear_widgets()
        for square, piece in enumerate(board.piece_arr):
            self.add_piece(piece,board.color_arr[square],square)

if __name__ == '__main__':
    ChessApp().run()

