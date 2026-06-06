import arcade
from arcade import Sound
from arcade.gui import UITextureButton, UIManager, UIFlatButton
from arcade.gui.widgets.layout import UIBoxLayout, UIAnchorLayout
import time

from pyglet.clock import Clock

class Timer():
    def __init__(self):
        self.time = 0
        self.started = False
        self.days = 1

    def update(self, delta_time: float):
        self.time += delta_time
    def start(self):
        self.started = True
    def real_time(self):
        self.days = int(1 + self.time//1440)
        if self.time >1440:
            t_time = self.time%1440
        else:
            t_time = self.time
        if len(str(int(t_time)%60))==1:

            rt = str(int(t_time)//60) + ':' + '0' + str(int(t_time)%60)
        else:
            rt = str(int(t_time)//60) + ':'+ str(int(t_time)%60)
        return rt
class Exit_Screen(arcade.View):
    def __init__(self):
        super().__init__()
        self.sp =arcade.SpriteList()
        self.trigger = True
    def setup(self):
        self.background_color = arcade.color.BLACK
        self.timer = Timer()
        self.sound = Sound('sounds/exit_sound.mp3', streaming=False)

    def on_update(self, delta_time: float):
        if self.timer.started:
            self.timer.update(delta_time)
        if 2<self.timer.time<3 and self.trigger:
            self.sound.play()
        if self.timer.time>5 and self.trigger:
            self.sound.play()
            self.trigger = False

    def on_draw(self):
        self.clear()

        txt = arcade.Text(text='Вы расстроили товарища Сталина', x=0, y=300, color=arcade.color.CRIMSON,
                              font_size=40,
                              width=400)

        if self.timer.time>6:

            arcade.exit()
        elif self.timer.time>3:
            txt.draw()



class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.manger = UIManager()
        self.main_anchor = UIAnchorLayout(x=0, y=0)
        self.main_layout = UIBoxLayout(vertical=True, space_between=40)
        self.main_anchor.add(self.main_layout)
        self.manger.add(self.main_anchor)
        self.main_sprite_list = arcade.SpriteList()
        self.manger.enable()


    def setup(self):
        self.background_color = arcade.color.BLACK
        self.background_texture = arcade.load_texture("textures/menu_background.png")
        self.setup_widgets()
        self.timer = Timer()
        self.timer.start()
    def on_update(self, delta_time: float):
        if self.timer.started:
            self.timer.update(delta_time)


    def setup_widgets(self):
        style = {
            'normal': UIFlatButton.UIStyle(
                font_size= 20,
                font_color= arcade.color.BLACK,
                bg = arcade.color.GRAY,
                border_width= 3,
                border= arcade.color.BLACK,
            ),
            'hover': UIFlatButton.UIStyle(
                font_size= 20,
                font_color= arcade.color.RED,
                bg = arcade.color.GRAY,
                border_width= 3,
                border= arcade.color.BLACK,
            ),
            'press': UIFlatButton.UIStyle(
                font_size= 20,
                font_color= arcade.color.BLACK,
                bg = arcade.color.CRIMSON_GLORY,
                border_width= 3,
                border= arcade.color.BLACK,
            )
        }
        start_button = UIFlatButton(text="Начать",width=200, height=80, style=style)
        exit_button = UIFlatButton(text="Выйти??",width=200, height=80, style=style, x=600, y=500)


        start_button.on_click = lambda event: (self.window.show_view(self.kab_view), self.kab_view.clock.start())
        exit_button.on_click = lambda event: (self.window.show_view(self.ex), self.ex.timer.start())
        self.main_layout.add(start_button)
        self.manger.add(exit_button)

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(self.background_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.manger.draw()