import pygame
from ..errors import ComponentDuplicateError


class ComponentsManager:
    """
    ComponentsManager
    Handle all the system and game components
    
    
    """
    def __init__(self):
        # {singletons, duplicates}
        self.system_components = {}
        self.game_components = {}

    def add_element(self, component: "Components"):
        # prevent duplicates of the system elements
        if isinstance(component, SystemComponents) and component.name.lower() not in self.system_components.keys():
            self.system_components[component.name.lower()] = component
        elif isinstance(component, GameComponents):
            self.game_components[component.name.lower()] = component
        else:
            raise ComponentDuplicateError()

    def update(self):
        for sys_comp in self.system_components.values():
            sys_comp.update()
        for game_comp in self.game_components.values():
            game_comp.update()
                
    def items(self):
        return self.system_components.items()

    def __getitem__(self, item):
        return self.system_components[item.lower()]
    

class Components:
    def __init__(self, gid=None, add: bool = False):
        self.components_manager: ComponentsManager = components_manager
        self.name = self.__class__.__name__ if not gid else gid
        if add:
            self.components_manager.add_element(self)
            
        # print(f"Setting up: {self.name}")

    def update(self):
        pass
    
    


class SystemComponents(Components):  # Singleton
    """
    System components that are singletons.
    Render, Camera, Inputs, Assets, etc.
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, gid=None, add=True):
        Components.__init__(self, gid, add)

    def __repr__(self):
        return f"System Component: '{self.__class__.__name__}()'"


class GameComponents(Components):
    """Game components that can be duplicates"""
    def __init__(self, gid=None, add=True):
        Components.__init__(self, gid, add)

    def __repr__(self):
        return f"Game Component: '{self.__class__.__name__}()'"


components_manager: ComponentsManager = ComponentsManager()
