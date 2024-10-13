from collections import defaultdict
from typing import Any, Optional

from src.shared import exceptions
from src.shared.debug import LOGGER

"""
ID ranges
System components: 1000 - 1999
"""


class ComponentManager:  # Singleton
  """ComponentsManager
  
  This is a singleton component that handles all the system and game components
  """
  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self):
    self.system_components_by_name: dict[str, SystemComponent] = {}
    self.game_components_by_name: dict[str,
                                       list[GameComponent]] = defaultdict(list)

  def add_element(self, component: 'Component') -> None:
    # Prevent duplicates of the system elements
    if isinstance(component, SystemComponent):
      if component.name not in self.system_components_by_name.keys():
        LOGGER.info(f'Adding component: {component}')
        LOGGER.info(f'Component Type: {type(component)}')
        self.system_components_by_name[component.name] = component
      else:
        LOGGER.error('Duplicate system component. Exiting...')
        raise exceptions.ComponentDuplicateError
    elif isinstance(component, GameComponent):
      self.game_components_by_name[component.name].append(component)
    else:
      raise exceptions.ComponentNotFoundError

  def update(self) -> None:
    for component in self.system_components_by_name.values():
      component.update()

  def get_system_components(self):
    return self.system_components_by_name.values()

  # TODO find a way to return correct type
  def get(self, name: str) -> Any:
    if name.lower() not in self.system_components_by_name.keys():
      raise exceptions.ComponentNotFoundError

    component = self.system_components_by_name[name.lower()]
    return component


class Component:
  components_manager = ComponentManager()

  def __init__(self, custom_id: Optional[int] = None, add=True):
    self.custom_id = custom_id
    self.name = self.__class__.__name__.lower()
    if add:
      self.components_manager.add_element(self)

    # LOGGER.info(f"Setting up: {self.name}")

  def update(self):
    pass


class SystemComponent(Component):  # Singleton
  """System components that are singletons.
  
  Render, Camera, Inputs, Assets, etc.
  """
  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, add=True):
    Component.__init__(self)

  def __repr__(self):
    return f"System Component: '{self.__class__.__name__}()'"


class GameComponent(Component):

  def __init__(self, add=True):
    Component.__init__(self)

  def __repr__(self):
    return f"Game Component: '{self.__class__.__name__}()'"
