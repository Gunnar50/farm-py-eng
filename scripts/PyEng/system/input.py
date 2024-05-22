import pygame
import sys
from ..element_manager.components import SystemComponents
from ..types import StrPath
import json


class KeyboardInput(SystemComponents):
    """
    Keyboard inputs for main keys

    """
    def __init__(self, key_mappings_path: StrPath):
        SystemComponents.__init__(self)
        with open(key_mappings_path, "r") as f:
            self.config = json.load(f)

    def update(self):
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
            
        if keys[pygame.K_LEFT]:
            pass


class MouseInput(SystemComponents):
    def __init__(self):
        SystemComponents.__init__(self)

