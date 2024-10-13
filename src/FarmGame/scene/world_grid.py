from typing import Optional

import pygame

from src.FarmGame.scene.tile import Tile
from src.PyEng.components.components import GameComponent
from src.PyEng.main.engine import Engine
from src.shared import serialisers


class Scene(GameComponent):
  WORLD_SIZE = 10

  def __init__(self) -> None:
    GameComponent.__init__(self)
    self.window = self.components_manager.get('window')
    self.world_grid = WorldGrid(self, Scene.WORLD_SIZE)

  def update(self):
    pass

  def render(self):
    self.world_grid.render(self.window.screen)


class WorldGrid(serialisers.Exportable, GameComponent):

  def __init__(self, scene: Scene, world_size: int) -> None:
    serialisers.Exportable.__init__(self)
    GameComponent.__init__(self)
    self.tiles: list[list[Tile]] = []
    self.scene = scene
    self.world_size = world_size
    self.tile_blueprints = self.components_manager.get(
        'GameManager').get_blueprint_database().tiles
    self.setup_grid(world_size)

  def setup_grid(self, size):
    for x in range(size):
      row = []
      for y in range(size):
        row.append(
            self.tile_blueprints.get('stone_path').create_instance((x, y),
                                                                   self))
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

  def render(self, screen: pygame.Surface):
    for x in range(self.world_size):
      for y in range(self.world_size):
        game_object = self.tiles[x][y]
        game_object.render_tile(screen, x, y)

    # # draw selected tile
    # if selected_pos is not None and game_state == "game":
    #   self.selection_tile.draw_tile(screen, *selected_pos)

  def get_serialiser(self) -> serialisers.Serialiser:
    return WorldGridSerialiser()


class WorldGridSerialiser(serialisers.Serialiser):

  def export(self, writer) -> None:
    raise NotImplementedError
