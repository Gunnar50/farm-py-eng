import dataclasses
from typing import Iterable, Optional, Union
import pygame
from PyEng.element_manager import components


@dataclasses.dataclass
class BaseModel(components.GameComponent):
  '''
  Type: class that belongs to
  Group: the group type (eg. tiles, crops)
  Layer: the layer that is rendered in (crops are rendered on top of tiles)
  
  '''
  label: str
  group: str
  layer: int
  images: tuple[pygame.Surface]


@dataclasses.dataclass
class Tile(BaseModel):
  pass


@dataclasses.dataclass
class Entity(BaseModel):
  pass


@dataclasses.dataclass
class Crop(Entity):
  # Grow time is amount in seconds
  grow_time: Iterable[int]
  amount: Union[int, Iterable[int]]
  next_growth_time: float = 0.0

