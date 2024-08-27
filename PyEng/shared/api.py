from dataclasses import dataclass
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


class MouseMapping(enum.Enum):
  MOUSE_LEFT = 'MOUSE_LEFT'
  MOUSE_RIGHT = 'MOUSE_RIGHT'
  MOUSE_MIDDLE = 'MOUSE_MIDDLE'


@dataclass
class BaseModel:
  pass


class Tile(BaseModel):
  label: str
  type_: str
  layer: int
  image_path: list[pygame.Surface]