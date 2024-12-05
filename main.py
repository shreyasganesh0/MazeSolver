from window import Window
from maze import Maze
from line import Line, Point
def main():
    width = 800
    height = 600
    wind = Window(width, height)
    startpoint = Point(30,30)
    maze = Maze(startpoint, wind)
    maze.draw_cells()
    wind.wait_for_close()
    print("in main")

if __name__ == "__main__":
    main()

