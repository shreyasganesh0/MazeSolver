from window import Window
from cell import Cell
from line import Line, Point
def main():
    width = 800
    height = 600
    wind = Window(width, height)
    startpoint = Point(30,30)
    cell = Cell(startpoint, wind, False,True, True, False)
    cell.draw()
    to_cell = Cell(Point(100,100),wind, False, True, True, True)
    to_cell.draw()
    cell.draw_path(to_cell, True)
    wind.wait_for_close()
    print("in main")

if __name__ == "__main__":
    main()

