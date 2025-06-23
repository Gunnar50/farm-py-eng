import pathlib
import sys
import time
from typing import Optional, Type

import pygame

from src.FarmGame.main.configs.build_config import BuildConfig
from src.PyEng.components.components import SystemComponent
from src.shared import api
from src.shared import io
from src.shared import key_mappings


class InputState:

  def __init__(
      self,
      label: str,
      type: api.InputType,
      input_name: str,
      input_id: int,
  ):
    self.label = label
    self.type = type
    self.input_name = input_name
    self.input_id = input_id

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

  def __init__(self, key_mappings_path: pathlib.Path,
               mapping_type: Type[key_mappings.MappingBase]):
    SystemComponent.__init__(self)
    self.config = io.load_model_from_json(key_mappings_path, api.InputConfig)
    self.input = {
        mapping_type(mapping.label): InputState(
            mapping.label, mapping.type, mapping.input_name,
            mapping.input_id) for mapping in self.config.config
    }
    self.mapping_type = mapping_type
    self.modifier_keys = []

    self.keyboard = Keyboard(self.input)
    self.mouse = Mouse(self.input)

  def pressed(
      self,
      key: key_mappings.MappingBase,
      modifier: Optional[key_mappings.MappingBase] = None,
  ) -> bool:
    if modifier:
      if modifier in self.modifier_keys:
        return self.input[key].just_pressed if key in self.input else False
    else:
      if not self.modifier_keys:
        return self.input[key].just_pressed if key in self.input else False

    return False

  def holding(self, key: key_mappings.MappingBase) -> bool:
    return self.input[key].pressed if key in self.input else False

  def released(self, key: key_mappings.MappingBase) -> bool:
    return self.input[key].just_released if key in self.input else False

  def update(self):
    for state in self.input.values():
      state.update()

    self.modifier_keys = [
        self.mapping_type(state.label)
        for state in self.input.values()
        if state.pressed
    ]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      self.keyboard.update(event)
      self.mouse.update(event)


class Keyboard:

  def __init__(self, input_config: dict[key_mappings.MappingBase, InputState]):
    self.input = input_config

  def update(self, event: pygame.event.Event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

      for state in self.input.values():
        if state.type == api.InputType.BUTTON and event.key == state.input_id:
          state.press()

    elif event.type == pygame.KEYUP:
      for state in self.input.values():
        if state.type == api.InputType.BUTTON and event.key == state.input_id:
          state.unpress()


class Mouse:

  def __init__(self, input_config: dict[key_mappings.MappingBase, InputState]):
    self.input = input_config
    self.position = api.Position(0, 0)
    self.ui_position = api.Position(0, 0)
    self.movement = api.Position(0, 0)

  def get_position(self) -> api.Position:
    return api.Position(self.position.x // BuildConfig.tile_width,
                        self.position.y // BuildConfig.tile_height)

  def update(self, event: pygame.event.Event):
    mx, my = pygame.mouse.get_pos()
    self.position = api.Position(mx // BuildConfig.scale_factor,
                                 my // BuildConfig.scale_factor)
    self.ui_x, self.ui_y = self.position.x // 2, self.position.y // 2

    if event.type == pygame.MOUSEBUTTONDOWN:
      for state in self.input.values():
        if state.type == api.InputType.MOUSE and event.button == state.input_id:
          state.press()

    elif event.type == pygame.MOUSEBUTTONUP:
      for state in self.input.values():
        if state.type == api.InputType.MOUSE and event.button == state.input_id:
          state.unpress()
