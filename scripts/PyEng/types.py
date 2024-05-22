import os
from typing import Tuple, Union, Sequence, TypeAlias
from pygame.math import Vector2
from pygame.color import Color

Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
StrPath: TypeAlias = str | os.PathLike[str]
