from collections.abc import Sized
from line import Line, Point
from window import Window
import math
class Cell:
    def __init__(self, point:Point,  window:Window, has_leftwall, has_topwall, has_bottomwall, has_rightwall):

        self._topleftx = point.x
        self._toplefty = point.y
        self._win = window
        self.has_leftwall = has_leftwall;
        self.has_bottomwall = has_bottomwall;
        self.has_topwall = has_topwall;
        self.has_rightwall = has_rightwall;
        self.side_len = math.sqrt(self._win.cell_size)
        self._centerx = self._topleftx + self.side_len//2
        self._centery = self._toplefty + self.side_len//2
        self.point1 = Point(self._topleftx +self.side_len, self._toplefty)
        self.point2 = Point(self._topleftx +self.side_len, self._toplefty+self.side_len)
        self.point3 = Point(self._topleftx , self._toplefty+self.side_len)
        self.point4 = Point(self._topleftx , self._toplefty)
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

    def draw_path(self, to_cell, undo = False):
        print(self._centerx, self._centery)
        print(to_cell._centerx, to_cell._centery)
        x_diff = abs(self._centerx - to_cell._centerx)
        y_diff = abs(self._centery - to_cell._centery)
        minx = min(self._centerx, to_cell._centerx)
        miny = min(self._centery, to_cell._centery)
        
        if (x_diff) and (y_diff):
            point_line = Point(x_diff+minx, miny)
        else:

            point_line = Point(x_diff+minx, y_diff+miny) 


        point_curr_cell = Point(self._centerx, self._centery)
        point_to_cell = Point(to_cell._centerx, to_cell._centery)
        
        print(point_line.x, point_line.y) 
        
        line1  = Line(point_curr_cell, point_line)
        
        line2 =  Line(point_to_cell, point_line)
        fill_color = "red" if undo else "gray"
        line1.draw(self._win.canvas, fill_color)
        line2.draw(self._win.canvas, fill_color)

