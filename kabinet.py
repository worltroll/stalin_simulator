import json

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
        self.central_layout = UIBoxLayout(x=200, y=50, space_between=20, vertical=False)
        self.manager.add(self.central_layout)
        self.manager.enable()
        self.this_event = {}

    def setup(self):
        self.background_color = arcade.color.RED
        self.background_texture = arcade.load_texture("textures/carpet.png")
        self.clock.time = 0.0
        self.setup_wigets()
        self.this_event = self.stalin.r_event()

    def newEvent(self):
        for p, i in self.stalin.parameters.items():
            if i <= -100:
                with open('saves/final_events.json', 'r') as file:
                    data = json.load(file)
                    self.end_game(data[p]["low"])
                break
            elif i >= 100:
                with open('saves/final_events.json', 'r') as file:
                    data = json.load(file)
                    self.end_game(data[p]["high"])
                break

        self.this_event = self.stalin.r_event()

    def end_game(self, text):
        pass

    def yes(self):
        for object in self.this_event['Yes']:
            self.stalin.parameters[object] += self.this_event['Yes'][object]
        self.newEvent()

    def no(self):
        for object in self.this_event['No']:
            self.stalin.parameters[object] += self.this_event['No'][object]
        self.newEvent()

    def setup_wigets(self):
        arcade.load_font("fonts/main_font.ttf")
        button_texture1 = arcade.load_texture("textures/button1_default.png")
        button_texture2 = arcade.load_texture("textures/button2_default.png")
        button_texture_press1 = arcade.load_texture("textures/button1_press.png")
        button_texture_press2 = arcade.load_texture("textures/button2_press.png")
        style_texture = {
            'normal': UITextureButton.UIStyle(
                font_size=20,
                font_color=arcade.color.GRAY,
                font_name='USSR STENCIL'
            ),
            'hover': UITextureButton.UIStyle(
                font_size=20,
                font_color=arcade.color.BLACK,
                font_name='USSR STENCIL'
            ),
            'press': UITextureButton.UIStyle(
                font_size=20,
                font_color=arcade.color.RED,
                font_name='USSR STENCIL'
            )
        }
        back_button = UITextureButton(width=100, height=100, style=style_texture, x=650, y=450,
                                      texture=button_texture2, texture_pressed=button_texture_press2)
        button_da = UITextureButton(text="Согласится", width=200, height=80, style=style_texture,
                                    texture=button_texture1, texture_pressed=button_texture_press1)
        button_net = UITextureButton(text="Отказаться", width=200, height=80, style=style_texture,
                                     texture=button_texture1, texture_pressed=button_texture_press1)
        button_da.on_click = lambda event: self.yes()
        button_net.on_click = lambda event: self.no()
        self.central_layout.add(button_da)
        self.central_layout.add(button_net)
        back_button.on_click = lambda event: (self.window.show_view(self.menu), self.clock.stop(),
                                              self.menu.manger.enable(), self.stalin.save_parameters())

        self.manager.add(back_button)

        self.emblem_paranoi = arcade.Sprite("textures/emblem_paranoi.png", center_x=55, center_y=470)
        self.emblem_nkvd = arcade.Sprite("textures/emblem_nkvd.png", center_x=55, center_y=350)
        self.emblem_person = arcade.Sprite("textures/emblem_person.png", center_x=55, center_y=230)

        self.emblems = arcade.SpriteList()
        self.emblems.append(self.emblem_paranoi)
        self.emblems.append(self.emblem_nkvd)
        self.emblems.append(self.emblem_person)

    def on_update(self, delta_time):
        if self.clock.started:
            self.clock.update(delta_time)

    def on_draw(self):
        self.clear()
        tme = arcade.Text(f"День {self.clock.days}, {self.clock.real_time()}", x=50, y=530, font_size=30,
                          font_name='USSR STENCIL', color=arcade.color.WHITE)

        arcade.draw_texture_rect(self.background_texture,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        tme.draw()
        event_title = arcade.Text(self.this_event['title'], x=200, y=370, font_size=25, color=arcade.color.WHITE,
                                  font_name='USSR STENCIL')
        event_text = arcade.Text(self.this_event['text'], x=150, y=300, font_size=25, font_name='USSR STENCIL',
                                 multiline=True, width=570)
        event_title.draw()
        event_text.draw()
        self.manager.draw()

        self.emblems.draw()
        paranoi_text = arcade.Text(str(self.stalin.parameters["paranoia"]), x=30, y=400, font_size=30,
                          font_name='USSR STENCIL', color=arcade.color.WHITE)
        paranoi_text.draw()

        nkvd_text = arcade.Text(str(self.stalin.parameters["nkvd"]), x=30, y=280, font_size=30,
                          font_name='USSR STENCIL', color=arcade.color.WHITE)
        nkvd_text.draw()

        person_text = arcade.Text(str(self.stalin.parameters["person"]), x=30, y=160, font_size=30,
                                   font_name='USSR STENCIL', color=arcade.color.WHITE)
        person_text.draw()

