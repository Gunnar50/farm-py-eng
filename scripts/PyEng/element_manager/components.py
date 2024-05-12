import pygame
from ..errors import ComponentDuplicateError


class ComponentsManager:
    def __init__(self):
        # {singletons, duplicates}
        self.comp = {"system": {}, "game": {}}

    def add_element(self, component: "Components"):
        # prevent duplicates of the system elements
        if isinstance(component, SystemComponents) and component.name not in self.comp["system"]:
            self.comp["system"][component.name] = component
        elif isinstance(component, GameComponents):
            self.comp["game"][component.name] = component
        else:
            raise ComponentDuplicateError(component)

    def update(self):
        for comp_type in self.comp:
            for component in self.comp[comp_type].values():
                component.update()

    def __getitem__(self, item):
        return self.comp["system"][item]
    
    def get_game_item(self, name: str):
        return self.comp["game"][name]


class Components:
    def __init__(self, gid=None, add: bool = False):
        self.components_manager = components_manager
        self.name = self.__class__.__name__ if not gid else gid
        if add:
            self.components_manager.add_element(self)

    def update(self):
        pass

    def remove_element(self):
        self.components_manager.remove_element(self)


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
        return f"{self.__class__.__name__}"


class GameComponents(Components):
    """Game components that can be duplicates"""
    def __init__(self, gid=None, add=True):
        Components.__init__(self, gid, add)

    def __repr__(self):
        return f"{self.__name__}"


components_manager = ComponentsManager()
