import enum
from typing import TYPE_CHECKING, Optional

import pygame

from src.FarmGame.main.configs.build_config import BuildConfig

if TYPE_CHECKING:
  from src.FarmGame.repository.game_components import TileBlueprint, TileType
  from src.FarmGame.scene.world_grid import WorldGrid


class Direction(enum.Enum):
  NORTH_WEST = (-1, -1)
  NORTH = (0, -1)
  NORTH_EAST = (1, -1)
  WEST = (-1, 0)
  EAST = (1, 0)
  SOUTH_WEST = (-1, 1)
  SOUTH = (0, 1)
  SOUTH_EAST = (1, 1)

  def __init__(self, relavite_x: int, relavite_y: int) -> None:
    self.relative_x = relavite_x
    self.relative_y = relavite_y

  def get_relative_pos(self) -> tuple[int, int]:
    return self.relative_x, self.relative_y


class GameObject:
  offset_x = (BuildConfig.window_width -
              (BuildConfig.map_width * BuildConfig.tile_width // 2) +
              (BuildConfig.map_height * BuildConfig.tile_width // 2)) // 2
  offset_y = (BuildConfig.window_height -
              (BuildConfig.map_height * BuildConfig.tile_height // 2)) // 2

  def __init__(
      self,
      position: tuple[int, int],
      world_grid: 'WorldGrid',
  ) -> None:
    self.x, self.y = position
    self.grid = world_grid


class Tile(GameObject):

  def __init__(
      self,
      position: tuple[int, int],
      world_grid: 'WorldGrid',
      components: 'TileBlueprint',
  ) -> None:
    GameObject.__init__(self, position, world_grid)
    self.components = components
    self.farmable = False

  def get_neighbours(self) -> list[Optional['Tile']]:
    return [
        self.get_neighbour(Direction.NORTH),
        self.get_neighbour(Direction.EAST),
        self.get_neighbour(Direction.SOUTH),
        self.get_neighbour(Direction.WEST),
    ]

  def get_neighbour(self, direction: Direction) -> Optional['Tile']:
    relative_x, relative_y = direction.get_relative_pos()
    grid_x = self.x + relative_x
    grid_y = self.y + relative_y
    return self.grid.get_tile(grid_x, grid_y)

  def get_tile_id(self) -> int:
    return (self.x * self.grid.world_size) + self.y

  def get_tile_type(self) -> 'TileType':
    return self.components.tile_type

  def render_tile(self, screen: pygame.Surface, x, y):
    screen_x = self.offset_x + x * BuildConfig.tile_width // 2 - y * BuildConfig.tile_width // 2 - BuildConfig.tile_width // 2
    screen_y = self.offset_y + x * (
        BuildConfig.tile_height - BuildConfig.tile_height / 2) // 2 + y * (
            BuildConfig.tile_height -
            BuildConfig.tile_height / 2) // 2 - BuildConfig.tile_height // 2

    if (-BuildConfig.tile_width <= screen_x <= BuildConfig.window_width) and (
        -BuildConfig.tile_height <= screen_y <= BuildConfig.window_height):
      screen.blit(self.components.images[0], (screen_x, screen_y))

  def __str__(self) -> str:
    return f'Tile({self.x}, {self.y})'

  def __repr__(self) -> str:
    return f'Tile({self.x}, {self.y}, {self.components.name})'
