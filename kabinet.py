import arcade
class Kabinet(arcade.View):
    def __init__(self):
        super().__init__()
        self.main_sprite_list = arcade.SpriteList()
    def setup(self):
        self.background_color = arcade.color.RED
        self.background_texture = arcade.load_texture("textures/kabinet_background.png")
    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
