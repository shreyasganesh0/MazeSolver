from cell import Cell
from line import Point
import time 
class Maze:
    def __init__(self, point, win, num_rows, num_cols):
        self.start_x = point.x
        self.start_y = point.y
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = win.width//num_cols
        self.cell_size_y = win.height//num_rows
        self._win = win
        self._cells = []

    def _create_cells(self):
    
        for i in range(self.start_y,int(self._win.height), self.cell_size_y):
            for j in range(self.start_x,int(self._win.width), self.cell_size_x):
                point = Point(j,i)
                cell = Cell(point, self._win.canvas, self.cell_size_x, self.cell_size_y, True, True, True, True)
                self._cells.append(cell)
    
    def draw_cells(self):
        self._create_cells()
        for cell in self._cells:
            cell.draw()
            self.animate()

    def animate(self):

        self._win.redraw()
        time.sleep(0.05)

