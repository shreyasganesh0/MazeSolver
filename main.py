from window import Window
from cell import Cell
from line import Line, Point
def main():
    width = 800
    height = 600
    wind = Window(width, height)
    
    for i in range(10, width, 2+wind.cell_size//(height//100)):
        for j in range(10,height, 2+wind.cell_size//(width//100)):
            print(i,j, "coords")
            startpoint = Point(j,i)
            cell = Cell(startpoint, wind, False,True, True, True)
            cell.draw()
    wind.wait_for_close()
    print("in main")

if __name__ == "__main__":
    main()

