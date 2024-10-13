import pygame

from src.FarmGame.scene.world_grid import Scene


class Session:
  """
  Parent Game class
  The main Game class should inherit from this
  class and override its methods
  """

  def __init__(self) -> None:
    self.scene = Scene()

  def update(self):
    self.scene.update()
    self.scene.render()
    # self.renderer.render_scene(self.scene)
