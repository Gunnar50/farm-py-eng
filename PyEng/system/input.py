import sys

import pygame

from PyEng.element_manager.components import SystemComponent
from PyEng.shared.types import StrPath
from PyEng.utils.io import load_json


class InputComponent(SystemComponent):

  def __init__(self, key_mappings_path: StrPath):
    SystemComponent.__init__(self)
    if key_mappings_path:
      self.config = load_json(key_mappings_path)
    else:
      self.config = {}


class KeyboardInput(InputComponent):
  """Keyboard inputs for main keys"""

  def __init__(self, key_mappings_path: StrPath):
    InputComponent.__init__(self, key_mappings_path)

  def update(self):
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if keys[pygame.K_ESCAPE]:
      pygame.quit()
      sys.exit()

    if keys[pygame.K_LEFT]:
      pass


class MouseInput(InputComponent):
  """Mouse inputs for main keys"""

  def __init__(self, key_mappings_path: StrPath):
    InputComponent.__init__(self, key_mappings_path)
