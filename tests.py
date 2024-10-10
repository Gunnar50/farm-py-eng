import dataclasses
import json
from typing import Type, TypeVar, Any, cast
import os
import pathlib

import pygame

from src.FarmGame.repository.game_files import GameFiles
from src.shared import exceptions
from src.shared.debug import LOGGER


@dataclasses.dataclass
class Blueprint:
  """
  Name: the unique name for this type of blueprint
  Group: the group this blueprint belongs (eg. tile, entities, crop)
  Layer: the layer that is rendered in (crops are rendered on top of tiles)
  Images: tuple containing the loaded images
  """
  name: str
  group: str
  layer: int
  images: list


@dataclasses.dataclass
class EntityBlueprint(Blueprint):
  stages: list[int]
  grow_time: int
  dry_out_time: int


BlueprintType = TypeVar('BlueprintType')


def load_json(file_path: pathlib.Path) -> dict[str, Any]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    LOGGER.error(f'File path {file_path} not found. Exiting...')
    raise exceptions.FilePathNotFound


def get_data_model(
    ParametersClass: Type[BlueprintType],
    file_path: pathlib.Path,
) -> BlueprintType:
  if not dataclasses.is_dataclass(ParametersClass):
    raise TypeError(f"{ParametersClass} is not a dataclass.")

  json_data = load_json(file_path)
  values = {}

  for field in dataclasses.fields(ParametersClass):
    attr = field.name
    if attr in json_data:
      value = json_data.pop(attr)
      if attr == 'images' and isinstance(value, list):
        value = [
            pygame.image.load(file_path.parent / image).convert_alpha()
            for image in value
        ]
      # Check if we need to convert anything to a list
      if (field.type is list or hasattr(field.type, '__origin__') and
          field.type.__origin__ is list) and not isinstance(value, list):
        values[attr] = [value]
      else:
        values[attr] = value

  try:
    result = ParametersClass(**values)
  except TypeError as e:
    LOGGER.error(f'Error initializing dataclass: {e}')
    raise ValueError(f'Error initializing dataclass: {e}')

  if json_data:
    LOGGER.warning(f'Remaining data that could not be loaded: {json_data}')

  return cast(BlueprintType, result)


get_data_model(
    EntityBlueprint,
    GameFiles.get_entities_folder() / 'crops' / 'carrot' /
    'entity_info_carrot.json')
