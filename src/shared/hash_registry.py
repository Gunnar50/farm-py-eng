import abc
from collections.abc import Iterable
from typing import Generic, Iterator, Optional, TypeVar

from src.shared import exceptions
from src.shared.debug import LOGGER

# Type variable RegistrableType, which is a subclass of Registrable
RegistrableType = TypeVar('RegistrableType', bound='Registrable')


class Registrable(abc.ABC):

  @abc.abstractmethod
  def get_name(self) -> str:
    pass


class HashRegistry(Generic[RegistrableType], Iterable):

  def __init__(self, registry_name: str = "hash"):
    self.registry_name = registry_name
    self.map: dict[str, RegistrableType] = {}

  def register(self, item: RegistrableType) -> None:
    if item.get_name() in self.map:
      raise exceptions.IllegalRegistryOverwrite(
          f"{self.registry_name} REGISTRY OVERWRITE: {item.get_name()}")
    else:
      self.map[item.get_name()] = item

  def register_all(self, *items: RegistrableType) -> None:
    for item in items:
      self.register(item)

  def get_null(self, name: str) -> Optional[RegistrableType]:
    item = self.map.get(name)
    if item is None:
      LOGGER.warning(
          f"No entry found in {self.registry_name} registry with ID: {name}")
    return item

  def get(self, string_id: str) -> RegistrableType:
    item = self.get_null(string_id)
    if item is None:
      raise exceptions.RegistryNotFoundException(
          f"No entry found in {self.registry_name} registry with ID: {string_id}"
      )
    return item

  def __iter__(self) -> Iterator[RegistrableType]:
    return iter(self.map.values())
