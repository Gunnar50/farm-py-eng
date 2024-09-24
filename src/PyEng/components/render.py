import pygame

from src.PyEng.components.components import SystemComponent
from src.shared import api
from src.shared.types import Coordinate


class Render(SystemComponent):
  """Render all the elements in the Window"""

  def __init__(self) -> None:
    SystemComponent.__init__(self)
    self.render_group: list[api.RenderObjects] = []

  def add_to_render_group(
      self,
      img: pygame.Surface,
      pos: Coordinate,
      dest_surf: pygame.Surface,
      layer: int,
  ) -> None:
    """Function to add elements to be rendered into a queue

    Args:
        img (pygame.Surface): The image/Surface that will be rendered
        pos (Coordinate): The position to render (x, y)
        dest_surf (pygame.Surface): The destination surface to render to (display, ui...)
        layer (int, optional): The layer (order) to render to.
    """
    self.render_group.append(
        api.RenderObjects(
            image=img,
            position=pos,
            destination_surface=dest_surf,
            layer=layer,
        ))

  def render(self):
    """Render every element in the render group to its respective destination surface"""
    for group in self.render_group:
      dest_surf = group.destination_surface
      dest_surf.blit(group.image, group.position)

  def update(self):
    self.render()
