from window import Window

def main():
    width = 800
    height = 600
    wind = Window(width, height)
    wind.wait_for_close()
    print("in main")

if __name__ == "__main__":
    main()

