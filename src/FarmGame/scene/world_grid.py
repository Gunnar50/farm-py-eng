import enum
from typing import Optional

from click import Option
from networkx import neighbors
from src.shared import serialisers


class Scene:
  pass


class TileContents:

  def __init__(self, tile: 'Tile') -> None:
    pass


class Direction(enum.Enum):
  NORTH_WEST = (-1, -1)
  NORTH = (0, -1)
  NORTH_EAST = (1, -1)
  WEST = (-1, 0)
  EAST = (1, 0)
  SOUTH_WEST = (-1, 1)
  SOUTH = (0, 1)
  SOUTH_EAST = (1, 1)

  def __init__(self, relavite_x: int, relavite_y, int) -> None:
    self.relative_x = relavite_x
    self.relative_y = relavite_y

  def get_relative_pos(self) -> tuple[int, int]:
    return self.relative_x, self.relative_y


class Tile:

  def __init__(self, x, y, world_grid: 'WorldGrid') -> None:
    self.x, self.y = x, y
    self.grid = world_grid
    self.contents = TileContents(self)

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

  def __str__(self) -> str:
    return f'Tile({self.x}, {self.y})'


class WorldGrid(serialisers.Exportable):

  def __init__(self, scene: Scene, world_size: int) -> None:
    serialisers.Exportable.__init__(self)
    self.tiles: list[list[Tile]] = []
    self.scene = scene
    self.world_size = world_size
    self.setup_grid(world_size)

  def setup_grid(self, size):
    for x in range(size):
      row = []
      for y in range(size):
        row.append(Tile(x, y, self))
      self.tiles.append(row)

  def add_tile(self, tile: Tile) -> None:
    self.tiles[tile.x][tile.y] = tile

  def get_tile_from_id(self, id: int):
    x, y = id // self.world_size, id % self.world_size
    return self.get_tile(x, y)

  def get_tile_at(self, x: float, y: float) -> Optional[Tile]:
    if x > 0 and y > 0:
      return self.get_tile(int(x), int(y))
    else:
      return None

  def get_tile(self, x: int, y: int) -> Optional[Tile]:
    if 0 < x < self.world_size and 0 < y < self.world_size:
      return self.tiles[x][y]
    else:
      return None

  def get_serialiser(self) -> serialisers.Serialiser:
    return WorldGridSerialiser()


class WorldGridSerialiser(serialisers.Serialiser):

  def export(self, writer) -> None:
    raise NotImplementedError
