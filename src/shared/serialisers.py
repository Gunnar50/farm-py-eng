import abc
from typing import Callable


class Serialiser(abc.ABC):

  @abc.abstractmethod
  def export(self) -> dict:
    pass
