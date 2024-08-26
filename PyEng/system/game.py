import pygame

from PyEng.element_manager.components import SystemComponent
from PyEng.system.assets import Assets
from PyEng.system.camera import Camera
from PyEng.system.input import KeyboardInput, MouseInput
from PyEng.system.render import Render
from PyEng.system.window import Window


class Game(SystemComponent):
  """
  Parent Game class
  The main Game class should inherit from this
  class and override its methods
  """

  def __init__(self):
    SystemComponent.__init__(self)
    self.window: Window
    self.render: Render
    self.assets: Assets
    self.camera: Camera
    self.mouseinput: MouseInput
    self.keyboardinput: KeyboardInput

  def load_data(self):
    pass

  def game_loop(self):
    pass

  def run(self):
    self.playing = True
    self.load_data()
    while self.playing:
      self.game_loop()
