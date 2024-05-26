import pygame
from ..element_manager.components import SystemComponents
from typing import Literal, List, TypeAlias, Tuple
from ..types import Coordinate

render_objects: TypeAlias = Tuple[pygame.Surface, Coordinate, pygame.Surface, int]

class Render(SystemComponents):
    """
    Render all the elements in the Window
    """
    def __init__(self) -> None:
        SystemComponents.__init__(self)
        self.render_group: List[render_objects] = []

    def add_to_render_group(self, img: pygame.Surface, pos: Coordinate,
                            dest_surf: pygame.Surface, layer: int) -> None:
        """Function to add elements to be rendered into a queue

        Args:
            img (pygame.Surface): The image/Surface that will be rendered
            pos (Coordinate): The position to render (x, y)
            dest_surf (pygame.Surface): The destination surface to render to (display, ui...)
            layer (int, optional): The layer (order) to render to.
        """
        self.render_group.append((img, pos, dest_surf, layer))
   

    def render(self):
        """Render every element in the render group to its respective destination surface"""
        for group in self.render_group:
            dest_surf: pygame.Surface = group[2]
            dest_surf.blit(group[0], group[1])

    def update(self):
        self.render()

