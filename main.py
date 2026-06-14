import arcade
from kabinet import Kabinet, Lose_view
from stalin import Stalin
from menu import Menu, Exit_Screen
class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
def main():
    window = Window(800, 600, "Stalin's simulator")
    exit_screen = Exit_Screen()

    kab = Kabinet()
    lose = Lose_view()
    men = Menu()
    men.kab_view = kab
    kab.menu = men
    kab.stalin = Stalin()
    kab.lose_view = lose
    men.ex = exit_screen
    lose.menu = men
    men.setup()

    kab.setup()
    lose.setup()
    exit_screen.setup()
    window.show_view(men)
    arcade.run()
if __name__ == "__main__":
    main()