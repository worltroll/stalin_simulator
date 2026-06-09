import arcade
from kabinet import Kabinet
from menu import Menu, Exit_Screen
class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
def main():
    window = Window(800, 600, "Stalin's simulator")
    exit_screen = Exit_Screen()
    kab = Kabinet()
    men = Menu()
    men.kab_view = kab
    kab.menu = men
    men.ex = exit_screen
    men.setup()
    kab.setup()
    exit_screen.setup()
    window.show_view(men)
    arcade.run()
if __name__ == "__main__":
    main()