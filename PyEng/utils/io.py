import json
import os
from typing import Any, Generator, Type, TypeVar
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


def get_class_name(text: str):
  if not text:
    return ""
  return text[0].upper() + text[1:].lower()


def load_files(file_path: StrPath) -> Generator[Any, Any, None]:
  if os.path.exists(file_path):
    with open(file_path, 'r') as f:
      remaining_data = json.load(f)
  else:
    raise exceptions.FilePathNotFound

  data: dict[str, Any]
  for data in remaining_data:
    values: dict[str, Any] = {}
    for attr, field in api.BaseModel.__dataclass_fields__.items():
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
      class_name = get_class_name(values['type_'])

      def repr_method(self):
        return f"{class_name}({', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())})"

      def init(self, **kwargs):
        for key, val in kwargs.items():
          setattr(self, key, val)

      model = type(
          class_name,
          (api.BaseModel,),
          {
              '__init__': init,
              '__repr__': repr_method
          },
      )
      instance = model(**{**values, **data})
      yield instance
    except pydantic.ValidationError:
      raise exceptions.InvalidParameters


# r = load_files('assets/data/crops.json')
# print(r)
# for a in r:
#   print(a.grow_time)
