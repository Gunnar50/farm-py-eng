import time

import pygame

from PyEng.element_manager.components import SystemComponent
from PyEng.shared.types import ColorValue, Coordinate


class Window(SystemComponent):
  """
  Window class

  Create a pygame window and it has the windows methods such as get_dt, update,
  clear, swap_buffers, etc...
  """

  def __init__(
      self,
      window_size: Coordinate,
      fullscreen: int,
      caption: str,
      fps: int,
      bg_colour: ColorValue,
  ):
    SystemComponent.__init__(self)
    pygame.init()
    self.fps = fps
    self.background_colour = bg_colour
    self.window_size = window_size
    self.start_time = time.time()

    self.screen = pygame.display.set_mode(window_size, fullscreen)
    pygame.display.set_caption(caption)
    self.clock = pygame.time.Clock()

    self.previous_frame = time.time()

  def get_dt(self):
    dt = time.time() - self.previous_frame
    self.previous_frame = time.time()
    return dt

  def update(self):
    self.clock.tick(self.fps)

  def clear(self):
    self.screen.fill(self.background_colour)

  def swap_buffers(self):
    pygame.display.flip()
