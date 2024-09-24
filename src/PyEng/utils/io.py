import json
import os
from typing import Any, Generator, Iterable

import pygame

from src.shared import db_models, exceptions
from src.shared.debug import LOGGER

# DataclassModelType = TypeVar('DataclassModelType',
#  bound=game_components.BaseModel)


def load_json(file_path: str):
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    LOGGER.error(f'File path {file_path} not found. Exiting...')
    raise exceptions.FilePathNotFound


def get_class_name(text: str):
  if not text:
    return ""
  return text[0].upper() + text[1:].lower()


def load_json_data(file_path: str) -> Generator[db_models.BaseModel, Any, None]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      remaining_data: Iterable[dict[str, Any]] = json.load(f)
  else:
    LOGGER.warning(f'File path not found: {file_path}')
    return

  for data in remaining_data:
    group = data.get('group', None)
    if group is None:
      LOGGER.warning('"group" key does not exist in config. Skipping...')
      continue

    model = getattr(db_models, group.capitalize(), None)
    if model is None:
      LOGGER.warning(f'model {group} not found in game_components. Skipping...')
      continue

    image_path = data.pop('image_path', None)
    if image_path is None:
      LOGGER.warning('"image_path" key not found in config. Skipping...')
      continue

    # Fix image path
    data['image_path'] = [f'assets/images/{path}' for path in image_path]

    yield model(**data)


def load_images(group: str, label: str, file_type: str = 'png'):
  path = f'assets/images/{group}'
  image_data: Iterable[pygame.Surface] = []
  for directory, _, file_path in os.walk(path):
    for asset in file_path:
      asset_type = asset.split('.')[-1]
      if asset_type == file_type and asset.startswith(label):
        asset_path = f'{directory}/{asset}'
        img = pygame.image.load(asset_path).convert_alpha()
        image_data.append(img)
  return directory, image_data
