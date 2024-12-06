from line import Line, Point
class Cell:
    def __init__(self, point:Point, canvas, x_size, y_size, has_leftwall, has_topwall, has_bottomwall, has_rightwall):

        self._topleftx = point.x
        self._toplefty = point.y
        self.canvas = canvas
        self.has_leftwall = has_leftwall;
        self.has_bottomwall = has_bottomwall;
        self.has_topwall = has_topwall;
        self.has_rightwall = has_rightwall;
        self._centerx = self._topleftx + x_size//2 
        self._centery = self._toplefty + y_size//2
        self.point1 = Point(self._topleftx +x_size//2, self._toplefty)
        self.point2 = Point(self._topleftx +x_size//2, self._toplefty+y_size//2)
        self.point3 = Point(self._topleftx , self._toplefty+ y_size//2)
        self.point4 = Point(self._topleftx , self._toplefty)
    
    def draw(self):
        print("in cell draw")
        if self.has_rightwall:
            lineobj = Line(self.point1, self.point2) 
            lineobj.draw(self.canvas, "White")

        if self.has_leftwall:
            lineobj = Line(self.point4, self.point3) 
            lineobj.draw(self.canvas, "White")
        if self.has_topwall:
            lineobj = Line(self.point1, self.point4) 
            lineobj.draw(self.canvas, "White")
        if self.has_bottomwall:
            lineobj = Line(self.point3, self.point2) 
            
            lineobj.draw(self.canvas, "White")

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
        line1.draw(self.canvas, fill_color)
        line2.draw(self.canvas, fill_color)

