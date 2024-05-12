import pygame
from ..element_manager.components import SystemComponents
import typing

class Render(SystemComponents):
    def __init__(self, game_type: typing.Literal["default", "isometric"]):
        SystemComponents.__init__(self)
        self.game_type = game_type
        self.render_group = []

    def add_to_render_group(self, img, pos, dest_surf, layer=0):
        if self.game_type == "isometric":
            self.render_group.append((img, pos, layer, dest_surf))
        else:
            # sort the list by the layers. layers is what goes on top of each other, 0 is the most visible layer and positive layer is blit behind
            self.render_group.append((img, pos, layer, dest_surf))
            self.render_group.sort(key=lambda x: x[3], reverse=True)

    def render(self):
        for group in self.render_group:
            group[2].blit(group[0], group[1])

    def update(self):
        self.render()


