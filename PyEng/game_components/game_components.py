from dataclasses import dataclass
import pygame
from PyEng.element_manager import components


@dataclass
class BaseModel(components.GameComponent):
  label: str
  type: str
  layer: int
  image_path: list[pygame.Surface]


class Tile(BaseModel):
  pass


class Entity(BaseModel):
  pass


class Crops(Entity):
  grow_time: list[int]
  amount: int
