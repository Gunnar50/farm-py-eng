import dataclasses
import os
import pathlib
from typing import Any, Type

from src.FarmGame.repository.game_components import (Blueprint, EntityBlueprint,
                                                     ItemBlueprint,
                                                     TileBlueprint)
from src.FarmGame.repository.game_files import GameFiles
from src.shared import exceptions, io
from src.shared.debug import LOGGER
from src.shared.hash_registry import HashRegistry, Registrable


@dataclasses.dataclass
class BlueprintLoader:
  file_prefix: str
  blueprint_type: Type[Blueprint]
  folder: pathlib.Path

  def load_folder(self, folder: pathlib.Path,
                  repository: HashRegistry[Any]) -> None:
    if not os.path.exists(folder):
      raise exceptions.FilePathNotFound(f'Path {folder} not found.')

    for item in folder.iterdir():
      if self.is_folder(item):
        self.load_file(item, repository)
      else:
        self.load_folder(item, repository)

  def load_file(self, folder: pathlib.Path,
                repository: HashRegistry[Blueprint]) -> None:
    try:
      info_json_file = self.get_info_file(folder)
      blueprint = io.get_data_model(self.blueprint_type, info_json_file)
      repository.register(blueprint)
    except Exception as ex:
      LOGGER.error(f'Failed to load blueprint: {folder}')
      # TODO: Push stack trace to a file
      LOGGER.error(f'Stack Trace: {str(ex)[:1000]}')

  def is_folder(self, folder: pathlib.Path) -> bool:
    # Check if any file in the folder ends with .json
    return any(file.is_file() and file.name.endswith(".json")
               for file in folder.iterdir())

  def get_info_file(self, folder: pathlib.Path) -> pathlib.Path:
    for file in folder.iterdir():
      if file.name.startswith(self.file_prefix):
        return file
    raise exceptions.InfoFileNotFound(f'No info file found for {folder.name}')


@dataclasses.dataclass
class EntityLoader(BlueprintLoader):
  file_prefix = 'entity_info'
  blueprint_type = EntityBlueprint
  folder = GameFiles.get_entities_folder()

  @classmethod
  def load(cls) -> HashRegistry[EntityBlueprint]:
    registry: HashRegistry[EntityBlueprint] = HashRegistry(
        registry_name='entities')
    loader = cls(cls.file_prefix, cls.blueprint_type, cls.folder)
    loader.load_folder(loader.folder, registry)
    return registry


@dataclasses.dataclass
class TilesLoader(BlueprintLoader):
  file_prefix = 'tile_info'
  blueprint_type = TileBlueprint
  folder = GameFiles.get_tiles_folder()

  @classmethod
  def load(cls) -> HashRegistry[TileBlueprint]:
    registry: HashRegistry[TileBlueprint] = HashRegistry(registry_name='tiles')
    loader = cls(cls.file_prefix, cls.blueprint_type, cls.folder)
    loader.load_folder(loader.folder, registry)
    return registry


@dataclasses.dataclass
class ItemLoader(BlueprintLoader):
  file_prefix = 'item_info'
  blueprint_type = ItemBlueprint
  folder = GameFiles.get_items_folder()

  @classmethod
  def load(cls) -> HashRegistry[ItemBlueprint]:
    registry: HashRegistry[ItemBlueprint] = HashRegistry(registry_name='items')
    loader = cls(cls.file_prefix, cls.blueprint_type, cls.folder)
    loader.load_folder(loader.folder, registry)
    return registry
