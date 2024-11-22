from window import Window
from line import Line, Point
def main():
    width = 800
    height = 600
    wind = Window(width, height)
    point1 = Point(10,200)
    point2= Point(20,20)
    line = Line(point1, point2)
    wind.draw_line(line, "White")
    wind.wait_for_close()
    print("in main")

if __name__ == "__main__":
    main()

