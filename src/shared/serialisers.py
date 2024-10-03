import abc
from typing import Callable


class Serialiser(abc.ABC):

  @abc.abstractmethod
  def export(self, writer) -> None:
    pass


class NoExport(Serialiser):

  def export(self, writer) -> None:
    pass


class Exportable(abc.ABC):

  @abc.abstractmethod
  def get_serialiser(self) -> Serialiser:
    return NoExport()
