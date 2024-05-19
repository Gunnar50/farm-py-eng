import pygame
import sys
from ..element_manager.components import SystemComponents


class KeyboardInput(SystemComponents):
    """
    Keyboard inputs for main keys

    """
    def __init__(self):
        SystemComponents.__init__(self)

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

