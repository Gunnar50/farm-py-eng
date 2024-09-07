import pygame

from PyEng.element_manager.components import SystemComponent
from PyEng.system.assets import Assets
from PyEng.system.camera import Camera
from PyEng.system.input import Input
from PyEng.system.render import Render
from PyEng.system.window import Window
import PyEng
from PyEng.shared.types import ColorValue, Coordinate


class Game(SystemComponent):
  """
  Parent Game class
  The main Game class should inherit from this
  class and override its methods
  """

  def __init__(
      self,
      *,
      window_size: Coordinate = (640, 480),
      fullscreen: int = 0,
      caption: str = "My Window",
      fps: int = 60,
      bg_colour: ColorValue = (0, 0, 0),
      assets_folder: str = "assets/data",
      key_mapping: str = "config",
  ):
    SystemComponent.__init__(self)
    PyEng.init(
        window_size=window_size,
        fullscreen=fullscreen,
        caption=caption,
        fps=fps,
        bg_colour=bg_colour,
        assets_folder=assets_folder,
        key_mapping=key_mapping,
    )

    self.window: Window
    self.render: Render
    self.assets: Assets
    self.camera: Camera
    self.input: Input

    # Add all components as attributes of this class
    for component in self.components_manager.components():
      setattr(self, component.name, component)
      self.__dict__[component.name] = component

  def load_data(self):
    pass

  def game_loop(self):
    pass

  def run(self):
    self.playing = True
    self.load_data()
    while self.playing:
      self.game_loop()
