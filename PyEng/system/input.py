import sys
import time

import pygame

from PyEng.element_manager.components import SystemComponent
from PyEng.shared import api
from PyEng.utils.io import load_json


class InputState:

  def __init__(self, mapping: api.KeyMappingModel):
    self.label = mapping.label
    self.type = mapping.type
    self.input = mapping.input_id

    self.pressed = False
    self.just_pressed = False
    self.just_released = False
    self.held_since = 0.0

  def update(self):
    self.just_pressed = False
    self.just_released = False

  def press(self):
    self.pressed = True
    self.just_pressed = True
    self.held_since = time.time()

  def unpress(self):
    self.pressed = False
    self.just_released = True


class Input(SystemComponent):

  def __init__(self, key_mappings_path: str):
    SystemComponent.__init__(self)
    self.config: list[api.KeyMappingModel] = load_json(key_mappings_path)
    self.input = {mapping.label: InputState(mapping) for mapping in self.config}

    self.keyboard = Keyboard()
    self.mouse = Mouse()

  def pressed(self, key: api.KeyMapping):
    return self.input[key.value].just_pressed if key in self.input else False

  def holding(self, key):
    return self.input[key].pressed if key in self.input else False

  def released(self, key):
    return self.input[key].just_released if key in self.input else False

  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
        if event.button == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()


class Keyboard:
  """Keyboard inputs for main keys"""


class Mouse:
  """Mouse inputs for main keys"""
