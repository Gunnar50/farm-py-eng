import abc
from typing import Optional, TypeVar, Generic, Iterator
from collections.abc import Iterable

from src.shared import exceptions
from src.shared.debug import LOGGER

# Type variable T, which is a subclass of Registrable
T = TypeVar('T', bound='Registrable')


class Id:

  @staticmethod
  def gen_for_access(string_id: str) -> 'Id':
    # Assuming a method to generate Id based on string_id
    return Id()

  def __init__(self):
    self.name = "some_id"  # Placeholder


class Registrable(abc.ABC):

  @abc.abstractmethod
  def get_id(self) -> Id:
    pass


class HashRegistry(Generic[T], Iterable):

  def __init__(self, registry_name: str = "hash"):
    self.registry_name = registry_name
    self.map: dict[Id, T] = {}

  def register(self, item: T) -> None:
    if item.get_id() in self.map:
      raise exceptions.IllegalRegistryOverwrite(
          f"{self.registry_name} REGISTRY OVERWRITE: {item.get_id().name}")
    else:
      self.map[item.get_id()] = item

  def register_all(self, *items: T) -> None:
    for item in items:
      self.register(item)

  def get(self, string_id: str) -> Optional[T]:
    id = Id.gen_for_access(string_id)
    item = self.map.get(id)
    if item is None:
      LOGGER.warning(
          f"No entry found in {self.registry_name} registry with ID: {string_id}"
      )
    return item

  def get_not_null(self, string_id: str) -> T:
    item = self.get(string_id)
    if item is None:
      raise exceptions.RegistryNotFoundException(
          f"No entry found in {self.registry_name} registry with ID: {string_id}"
      )
    return item

  def get_by_id(self, id: Id) -> T:
    item = self.map.get(id)
    if item is None:
      raise exceptions.RegistryNotFoundException(
          f"No entry found in {self.registry_name} registry with ID: {id}")
    return item

  def __iter__(self) -> Iterator[T]:
    return iter(self.map.values())
