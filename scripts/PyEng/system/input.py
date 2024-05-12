import pygame
import sys
from ..element_manager.components import SystemComponents


class KeyInput(SystemComponents):
    def __init__(self):
        SystemComponents.__init__(self)
        self.keys = pygame.key.get_pressed()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if self.keys[pygame.QUIT]:
            pass


class MouseInput(SystemComponents):
    def __init__(self):
        SystemComponents.__init__(self)

