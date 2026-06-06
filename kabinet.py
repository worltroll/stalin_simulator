import arcade
from menu import Timer
class Kabinet(arcade.View):
    def __init__(self):
        super().__init__()
        self.main_sprite_list = arcade.SpriteList()
        self.clock = Timer()
    def setup(self):
        self.background_color = arcade.color.RED
        self.background_texture = arcade.load_texture("textures/kabinet_background.png")
        self.clock.time = 1409.0
    def prent(self):
        print('g')
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
