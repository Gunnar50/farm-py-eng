from dataclasses import dataclass
import pygame
from PyEng.element_manager import components


@dataclass
class BaseModel(components.GameComponent):
  label: str
  group: str
  layer: int
  image_path: str
  image_surface: list[pygame.Surface]


@dataclass
class Tile(BaseModel):
  pass


@dataclass
class Entity(BaseModel):
  pass


@dataclass
class Crops(Entity):
  grow_time: list[int]
  amount: int
