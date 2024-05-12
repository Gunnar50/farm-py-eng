import pygame
import time
from ..element_manager.components import SystemComponents


class Window(SystemComponents):
    def __init__(self, window_size, fullscreen, caption, fps, bg_colour):
        SystemComponents.__init__(self)
        pygame.init()
        self.fps = fps
        self.background_colour = bg_colour
        self.window_size = window_size
        self.start_time = time.time()

        self.screen = pygame.display.set_mode(window_size, fullscreen)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        self.previous_frame = time.time()

    def get_dt(self):
        dt = time.time() - self.previous_frame
        self.previous_frame = time.time()
        return dt

    def update(self):
        self.clock.tick(self.fps)
        pygame.display.flip()

    def clear(self):
        self.screen.fill(self.background_colour)






