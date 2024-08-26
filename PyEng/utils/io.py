import json
import os
from typing import Any, Type

import pydantic
from PyEng.shared import exceptions

from PyEng.shared.types import PydanticModelType, StrPath
from PyEng.shared import api


def load_json(file_path: StrPath):
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    return {}


def load(
    file_path: StrPath,
    ParametersClass: Type[PydanticModelType],
) -> list[PydanticModelType]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      remaining_data = json.load(f)
  else:
    raise exceptions.FilePathNotFound

  results = []
  for data in remaining_data:
    values: dict[str, Any] = {}
    for attr, field in ParametersClass.model_fields.items():
      if attr in data:
        value = data.pop(attr)
        if (str(field.annotation).startswith('list[') and
            not isinstance(value, list)):
          values[attr] = [value]
        else:
          values[attr] = value
    try:
      results.append(ParametersClass(**values))
    except pydantic.ValidationError:
      raise exceptions.InvalidParameters
  print(results)
  return results


load('assets/data/tiles.json', api.Tile)
