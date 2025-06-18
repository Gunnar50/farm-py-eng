import time

import pygame

from src.FarmGame.main.configs.build_config import BuildConfig
from src.PyEng.components.components import SystemComponent


class Window(SystemComponent):
  """
  Window class

  Create a pygame window and it has the windows methods such as get_dt, update,
  clear, swap_buffers, etc...
  """

  def __init__(
      self,
      window_width: int,
      window_height: int,
      fullscreen: int,
      caption: str,
      fps: int,
      vsync: bool,
      background_colour: tuple[int, int, int],
  ):
    SystemComponent.__init__(self)
    pygame.init()
    self.fps = fps
    self.background_colour = background_colour
    self.window_width = window_width
    self.window_height = window_height
    self.start_time = time.time()

    self.screen = pygame.display.set_mode(size=(window_width, window_height),
                                          flags=fullscreen,
                                          vsync=vsync)
    self.display = pygame.Surface(
        (window_width // BuildConfig.scale_factor,
         window_height // BuildConfig.scale_factor)).convert_alpha()
    self.debug_display = pygame.Surface(
        (window_width, window_height)).convert_alpha()

    pygame.display.set_caption(caption)
    self.clock = pygame.time.Clock()

    self.previous_frame = time.time()

  def get_width(self) -> int:
    return self.window_width

  def get_height(self) -> int:
    return self.window_height

  def get_dt(self):
    dt = time.time() - self.previous_frame
    self.previous_frame = time.time()
    return dt

  def update(self):
    self.clock.tick(self.fps)
    self.swap_buffers()
    self.clear()

  def clear(self):
    self.display.fill(self.background_colour)
    self.debug_display.fill((0, 0, 0, 0))

  def swap_buffers(self):
    scaled_display = pygame.transform.scale(self.display,
                                            self.screen.get_size())
    self.screen.blit(scaled_display, (0, 0))
    self.screen.blit(self.debug_display, (0, 0))
    pygame.display.flip()
