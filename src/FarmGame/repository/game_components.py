import dataclasses
import enum
import random
from typing import Iterable, Union

import pygame

from src.FarmGame.scene.tile import Tile
from src.FarmGame.scene.world_grid import WorldGrid
from src.shared.hash_registry import Registrable


class TileType(enum.Enum):
  GRASS = 'grass'
  SOIL = 'soil'
  PATH = 'path'
  SELECTION = 'selection'
  STONE_PATH = 'stone_path'


@dataclasses.dataclass
class Blueprint(Registrable):
  """
  Name: the unique name for this type of blueprint
  Group: the group this blueprint belongs (eg. tile, entities, crop)
  Layer: the layer that is rendered in (crops are rendered on top of tiles)
  Images: tuple containing the loaded images
  """
  name: str
  group: str
  layer: int
  images: tuple[pygame.Surface]

  def get_name(self) -> str:
    return self.name


@dataclasses.dataclass
class EntityBlueprint(Blueprint):
  tile_type: TileType
  stages: list[int]
  grow_time: int
  dry_out_time: int

  def create_instance(self):
    pass


@dataclasses.dataclass
class ItemBlueprint(Blueprint):
  stages: list[int]
  grow_time: int


@dataclasses.dataclass
class TileBlueprint(Blueprint):
  tile_type: TileType

  def create_instance(self, position: tuple[int, int], grid: WorldGrid) -> Tile:
    return Tile(position, grid, self)


@dataclasses.dataclass
class Crop(EntityBlueprint):
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

  def update(self):
    # TODO - get DT from window
    dt = 1.0

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
