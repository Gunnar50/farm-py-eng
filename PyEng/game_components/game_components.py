from dataclasses import dataclass
from typing import Optional
import pygame
from PyEng.element_manager import components


@dataclass
class BaseModel(components.GameComponent):
  '''
  Type: class that belongs to
  Group: the group type (eg. tiles, crops)
  Layer: the layer that is rendered in (crops are rendered on top of tiles)
  
  '''
  label: str
  group: str
  layer: int
  image_path: list[str]
  image: Optional[list[pygame.Surface]] = None

  # Executes right after the __init__ method
  def __post_init__(self):
    # Generate image
    if self.image is None:
      # TODO - update tile size
      self.image = [
          pygame.transform.scale(pygame.image.load(image), (100, 100))
          for image in self.image_path
      ]


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
