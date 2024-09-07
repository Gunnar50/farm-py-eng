import enum

import pydantic
import pygame

from PyEng.shared.types import Coordinate


class RenderObjects(pydantic.BaseModel):
  image: pygame.Surface
  position: Coordinate
  destination_surface: pygame.Surface
  layer: int

  # This is to allow pygame.Surface to be passed as a type
  model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)


class KeyMapping(enum.Enum):
  QUIT = 'quit'
  RIGHT = 'right'
  LEFT = 'left'
  UP = 'up'
  DOWN = 'down'
  LEFT_CLICK = 'left_click'
  MIDDLE_CLICK = 'middle_click'
  RIGHT_CLICK = 'right_click'


class KeyMappingModel(pydantic.BaseModel):
  label: KeyMapping
  type: str
  input_id: str


class GroupType(enum.Enum):
  TILES = 'tiles'
  CROPS = 'crops'
