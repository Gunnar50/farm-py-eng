from typing import Iterable, Optional

import pydantic
import pygame


class BaseModel(pydantic.BaseModel):
  label: str
  group: str
  layer: int
  image_path: Iterable[str]
  images: Optional[Iterable[pygame.Surface]] = None

  # This is to allow pygame.Surface to be passed as a type
  model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)

  # Use model_validator to process the image loading after initialization
  @pydantic.model_validator(mode="after")
  def load_images(cls, values):
    # Access image_path directly from the model instance
    if values.images is None:
      values.images = [
          pygame.transform.scale(pygame.image.load(path), (100, 100))
          for path in values.image_path
      ]
    return values


class Tile(BaseModel):
  pass


class Crop(BaseModel):
  grow_time: Iterable[int]
  amount: int
