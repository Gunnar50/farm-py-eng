import os
from typing import Sequence, TypeAlias, TypeVar, Union

import pydantic
import pygame

Coordinate = Union[tuple[float, float], Sequence[float]]
RGBAOutput = tuple[int, int, int, int]
ColorValue = Union[pygame.color.Color, int, str, tuple[int, int, int],
                   RGBAOutput, Sequence[int]]
StrPath: TypeAlias = Union[str, os.PathLike[str]]
PydanticModelType = TypeVar('PydanticModelType', bound=pydantic.BaseModel)
