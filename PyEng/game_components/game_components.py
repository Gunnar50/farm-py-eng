import dataclasses
import random
from typing import Iterable, Union
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

  def __post_init__(self):
    self.current_stage = 0
    if isinstance(self.amount, Iterable):
      self.amount = random.randint(*self.amount)
    self.current_stage_time = 0.0
    self.ready_stage = len(self.images) - 1
    self.generate_stage_duration()

  def generate_stage_duration(self):
    self.next_growth_time = random.uniform(*self.grow_time) * 1000

  def is_fully_grown(self):
    return self.current_stage == self.ready_stage

  def update(self, dt):
    # Check if is fully grown
    if self.is_fully_grown():
      return

    self.current_stage_time += dt

    if self.current_stage_time >= self.next_growth_time:
      self.next_stage()

  def next_stage(self):
    self.current_stage += 1
    self.current_stage_time = 0.0
    self.generate_stage_duration()
