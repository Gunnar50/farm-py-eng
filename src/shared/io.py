import dataclasses
import enum
import json
import pathlib
from typing import Any, Type, TypeVar, cast, get_origin

import pydantic
import pygame

from src.shared import exceptions
from src.shared import serialisers
from src.shared.debug import LOGGER

BlueprintType = TypeVar('BlueprintType')
ModelType = TypeVar('ModelType', bound=pydantic.BaseModel)


def export_data(data: Any) -> Any:
  if isinstance(data, list):
    return [export_data(item) for item in data]

  elif isinstance(data, dict):
    return {key: export_data(value) for key, value in data.items()}

  elif isinstance(data, serialisers.Serialiser):
    return export_data(data.export())

  elif (isinstance(data, (int, str, float, bool))):
    return data

  return None


def write_data(file_path: pathlib.Path, data: Any) -> None:
  with open(file_path, 'w') as f:
    f.write(str(data))


def write_json(file_path: pathlib.Path, data: Any) -> None:
  with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)


def load_json(file_path: pathlib.Path) -> Any:
  if file_path.exists():
    with open(file_path, 'r') as f:
      return json.load(f)
  else:
    raise exceptions.FilePathNotFound(
        f'The following file path was not found: {file_path}')


def load_model_from_json(file_path: pathlib.Path,
                         model: Type[ModelType]) -> ModelType:
  data = load_json(file_path)
  return model.model_validate(data)


def get_data_model(
    ParametersClass: Type[BlueprintType],
    file_path: pathlib.Path,
) -> BlueprintType:
  if not dataclasses.is_dataclass(ParametersClass):
    raise exceptions.NotDataclass(f'"{ParametersClass}" is not a dataclass.')

  json_data = load_json(file_path)
  values = {}

  for field in dataclasses.fields(ParametersClass):
    attr = field.name
    if attr in json_data:
      value = json_data.pop(attr)
      # Handle enum fields: convert the value to the correct enum type
      if isinstance(field.type, enum.EnumMeta):
        value = field.type(value)

      # Load the images into the blueprint
      elif attr == 'images' and isinstance(value, list):
        value = [
            pygame.image.load(file_path.parent / image).convert_alpha()
            for image in value
        ]

      # Check if we need to convert anything to a list
      if get_origin(field.type) is list and not isinstance(value, list):
        values[attr] = [value]
      else:
        values[attr] = value

  try:
    result = ParametersClass(**values)
  except TypeError:
    context = {
        'ParametersClass': ParametersClass,
        'values': values,
    }
    raise exceptions.FailedToGetDataModel(f'Error initialising model', context)

  if json_data:
    LOGGER.warning(f'Remaining data that could not be loaded: {json_data}')

  return cast(BlueprintType, result)
