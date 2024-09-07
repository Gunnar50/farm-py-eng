from typing import Optional
from PyEng.shared import exceptions
from PyEng.shared.debug import LOGGER
"""
ID ranges
System components: 1000 - 1999
Game components: 2000 - 2999
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
    # {singletons, duplicates}
    self.system_components_by_id: dict[int, SystemComponent] = {}
    self.game_components_by_id: dict[int, GameComponent] = {}

  def add_element(self, component: 'Component'):
    # Prevent duplicates of the system elements
    if isinstance(component, SystemComponent):
      if component.id not in self.system_components_by_id.keys():
        self.system_components_by_id[component.id] = component
      else:
        LOGGER.error('Duplicate system component. Exiting...')
        raise exceptions.ComponentDuplicateError
    elif isinstance(component, GameComponent):
      self.game_components_by_id[component.id] = component
    else:
      raise exceptions.ComponentNotFoundError

  def update(self):
    for sys_comp in self.system_components_by_id.values():
      sys_comp.update()
    for game_comp in self.game_components_by_id.values():
      game_comp.update()

  def components(self):
    return self.system_components_by_id.values()

  def __getitem__(self, _id: int):
    return self.system_components_by_id[_id]


class Component:
  components_manager = ComponentManager()

  def __init__(self, _id: int, add: bool = False):
    self.id = _id
    self.name = self.__class__.__name__.lower()
    if add:
      self.components_manager.add_element(self)

    # print(f"Setting up: {self.name}")

  def update(self):
    pass


class SystemComponent(Component):  # Singleton
  """System components that are singletons.
  
  Render, Camera, Inputs, Assets, etc.
  """
  __instance = None
  _id = 1000

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      SystemComponent._id += 1
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, add=True):
    Component.__init__(self, self.__class__._id, add)

  def __repr__(self):
    return f"System Component: '{self.__class__.__name__}()'"


class GameComponent(Component):
  """Game components that can be duplicates"""
  _id = 2000

  def __new__(cls, *args, **kwargs):
    GameComponent._id += 1
    return super().__new__(cls)

  def __init__(self, add=True):
    Component.__init__(self, self.__class__._id, add)

  def __repr__(self):
    return f"Game Component: '{self.__class__.__name__}()'"
