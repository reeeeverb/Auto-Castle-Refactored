from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

class Knight(Widget):
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

