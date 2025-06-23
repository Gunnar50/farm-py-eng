import dataclasses
import enum
from typing import Iterator, Self

import pydantic
import pygame

from src.shared import serialisers
from src.shared import types


class RenderObjects(pydantic.BaseModel):
  image: pygame.Surface
  position: types.Coordinate
  destination_surface: pygame.Surface
  layer: int

  # This is to allow pygame.Surface to be passed as a type
  model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)


class KeyMappingModel(pydantic.BaseModel):
  label: str
  type: str
  input_id: str


class GroupType(enum.Enum):
  TILES = 'tiles'
  CROPS = 'crops'


class KeyMapping(enum.Enum):
  QUIT = 'quit'
  RIGHT = 'right'
  LEFT = 'left'
  UP = 'up'
  DOWN = 'down'
  LEFT_CLICK = 'left_click'
  MIDDLE_CLICK = 'middle_click'
  RIGHT_CLICK = 'right_click'


class InputType(enum.Enum):
  BUTTON = 'button'
  MOUSE = 'mouse'


class InputMappings(pydantic.BaseModel):
  label: str
  type: InputType
  input_name: str
  input_id: int


class InputConfig(pydantic.BaseModel):
  config: list[InputMappings]


@dataclasses.dataclass
class Movement:
  x: int
  y: int

  def __add__(self, other: 'Movement') -> Self:
    return type(self)(self.x + other.x, self.y + other.y)


@dataclasses.dataclass
class Position(Movement, serialisers.Serialiser):

  def __iter__(self) -> Iterator[int]:
    return iter((self.x, self.y))

  def export(self) -> dict[str, int]:
    return {'x': self.x, 'y': self.y}


class TileType(enum.Enum):
  GRASS = 'grass'
  DIRT = 'dirt'
  BUSH = 'bush'


class TileImport(pydantic.BaseModel):
  position: Position
  variant: int
  layer: int
  tile_type: TileType


class WorldGridImport(pydantic.BaseModel):
  tile_map: list[TileImport]
