from collections.abc import Sized
from line import Line, Point
from window import Window
import math
class Cell:
    def __init__(self, point:Point,  window:Window, has_leftwall, has_topwall, has_bottomwall, has_rightwall):

        self._centerx = point.x
        self._centery = point.y
        self._win = window
        self.has_leftwall = has_leftwall;
        self.has_bottomwall = has_bottomwall;
        self.has_topwall = has_topwall;
        self.has_rightwall = has_rightwall;

        side_len = math.sqrt(self._win.cell_size)
        self.point1 = Point(self._centerx +side_len, self._centery)
        self.point2 = Point(self._centerx +side_len, self._centery+side_len)
        self.point3 = Point(self._centerx , self._centery+side_len)
        self.point4 = Point(self._centerx , self._centery)
    def draw(self):
        if self.has_rightwall:
            lineobj = Line(self.point1, self.point2) 
            lineobj.draw(self._win.canvas, "White")

        if self.has_leftwall:
            lineobj = Line(self.point4, self.point3) 
            lineobj.draw(self._win.canvas, "White")
        if self.has_topwall:
            lineobj = Line(self.point1, self.point4) 
            lineobj.draw(self._win.canvas, "White")
        if self.has_bottomwall:
            lineobj = Line(self.point3, self.point2) 
            lineobj.draw(self._win.canvas, "White")
