import json
import os
from typing import Any, Type, TypeVar
import pygame
import pydantic
from PyEng.shared import exceptions

from PyEng.shared.types import StrPath
from PyEng.shared import api

DataclassModelType = TypeVar('DataclassModelType', bound=api.BaseModel)


def load_json(file_path: StrPath):
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    return {}


def load(
    file_path: StrPath,
    ParametersClass: Type[DataclassModelType],
) -> list[DataclassModelType]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      remaining_data = json.load(f)
  else:
    raise exceptions.FilePathNotFound

  results = []
  for data in remaining_data:
    values: dict[str, Any] = {}
    for attr, field in ParametersClass.__dataclass_fields__.items():
      if attr in data:
        value = data.pop(attr)
        if (str(field.type).startswith('list[') and
            not isinstance(value, list)):
          values[attr] = [value]
        elif attr == 'image_path':
          values[attr] = [pygame.image.load(img) for img in value]
        else:
          values[attr] = value

    try:
      results.append(ParametersClass(**values))
    except pydantic.ValidationError:
      raise exceptions.InvalidParameters
  return results


load('assets/data/tiles.json', api.Tile)
