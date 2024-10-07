import pygame

from src.FarmGame.scene.render import Render
from src.FarmGame.scene.world_grid import Scene


class Game:
  """
  Parent Game class
  The main Game class should inherit from this
  class and override its methods
  """

  def __init__(self, renderer: Render) -> None:
    self.renderer = renderer
    self.scene = Scene()
    self.scene.set_game(self)

  def update(self):
    self.scene.update()
    self.renderer.render_scene(self.scene)
