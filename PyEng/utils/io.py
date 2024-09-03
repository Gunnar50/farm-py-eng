import json
import os
from typing import Any, Generator, TypeVar
import pygame
import pydantic
from PyEng.shared import exceptions

from PyEng.shared.types import StrPath
from PyEng.game_components import game_components

DataclassModelType = TypeVar('DataclassModelType',
                             bound=game_components.BaseModel)


def load_json(file_path: StrPath):
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    return {}


def get_class_name(text: str):
  if not text:
    return ""
  return text[0].upper() + text[1:].lower()


def load_json_data(file_path: StrPath) -> Generator[Any, Any, None]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      remaining_data = json.load(f)
  else:
    raise exceptions.FilePathNotFound

  data: dict[str, Any]
  for data in remaining_data:
    if 'type' not in data:
      print(f'Warning: "type" not found in data: {data}')
      continue

    # Get the class name from the group attribute
    class_name = data.pop('type').capitalize()

    # Get the correct class from game_components
    model = getattr(game_components, class_name, None)
    if model is None:
      print(f'Warning: model {class_name} not found in game_components.')
      continue

    # Unpack the attributes into the model class
    values: dict[str, Any] = {}
    print(model.__dataclass_fields__.keys())
    for attr in model.__dataclass_fields__.keys():
      if attr in data:
        value = data.pop(attr)
        values[attr] = value

    # Create the images

    # assets/images/tiles/grass_tile.png
    directory, image_data = load_images(values['group'], values['label'])
    values['image_path'] = directory
    values['image_surface'] = image_data

    if data:
      print(f'Warning: Extra data found in config file: {data}')

    yield model(**values)


def load_images(group: str, label: str, file_type: str = 'png'):
  path = f'assets/images/{group}'
  image_data: list[pygame.Surface] = []
  for directory, _, file_path in os.walk(path):
    for asset in file_path:
      asset_type = asset.split('.')[-1]
      if asset_type == file_type and asset.startswith(label):
        asset_path = f'{directory}/{asset}'
        img = pygame.image.load(asset_path).convert_alpha()
        image_data.append(img)
  return directory, image_data


# def repr_method(self):
#   return f"{class_name}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"

# r = load_files('assets/data/crops.json')
# print(r)
# for a in r:
#   print(a.grow_time)
