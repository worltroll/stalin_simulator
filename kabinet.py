import arcade
from arcade.gui import UITextureButton, UIManager, UIFlatButton
from arcade.gui.widgets.layout import UIBoxLayout, UIAnchorLayout
from menu import Timer
class Kabinet(arcade.View):
    def __init__(self):
        super().__init__()
        self.main_sprite_list = arcade.SpriteList()
        self.clock = Timer()
        self.manager = UIManager()
        self.central_layout = UIBoxLayout(x=50, y=300, space_between=20, vertical=False)
        self.manager.add(self.central_layout)
        self.manager.enable()
    def setup(self):
        self.background_color = arcade.color.RED
        self.background_texture = arcade.load_texture("textures/kabinet_background.png")
        self.clock.time = 1409.0
        self.setup_wigets()
    def setup_wigets(self):
        button_texture1 = arcade.load_texture("textures/button1_default.png")
        button_texture2 = arcade.load_texture("textures/button2_default.png")
        button_texture_press1 = arcade.load_texture("textures/button1_press.png")
        button_texture_press2 = arcade.load_texture("textures/button2_press.png")
        style_texture = {
            'normal': UITextureButton.UIStyle(
                font_size=16,
                font_color=arcade.color.GRAY,

            ),
            'hover': UITextureButton.UIStyle(
                font_size=16,
                font_color=arcade.color.BLACK,

            ),
            'press': UITextureButton.UIStyle(
                font_size=16,
                font_color=arcade.color.RED,

            )
        }
        back_button = UITextureButton(text="Назад", width=100, height=80, style=style_texture, x=600, y=500,
                                      texture=button_texture2, texture_pressed=button_texture_press2)
        ucraine_button = UITextureButton(text="Выдумать Украину", width=220, height=80, style=style_texture,
                                      texture=button_texture1, texture_pressed=button_texture_press1)
        golodomor_button = UITextureButton(text="Начать Голодомор", width=220, height=80, style=style_texture,
                                      texture=button_texture1, texture_pressed=button_texture_press1)
        industialization_button = UITextureButton(text="Усиленная индустриализация", width=220, height=80, style=style_texture,
                                      texture=button_texture1, multiline=True, texture_pressed=button_texture_press1)
        self.central_layout.add(ucraine_button)
        self.central_layout.add(golodomor_button)
        self.central_layout.add(industialization_button)
        back_button.on_click = lambda event: (self.window.show_view(self.menu), self.clock.stop(), self.menu.manger.enable())
        self.manager.add(back_button)
    def on_update(self, delta_time):
        if self.clock.started:
            self.clock.update(delta_time)
    def on_draw(self):
        self.clear()
        tme = arcade.Text( 'Время ' + self.clock.real_time(), color=arcade.color.BLACK, x=50, y=500, font_size=40)
        day = arcade.Text(f'День {self.clock.days}', x=50, y=550, font_size=40, color=arcade.color.BLACK)

        arcade.draw_texture_rect(self.background_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        tme.draw()
        day.draw()
        self.manager.draw()
