import pygame
import time
from ..element_manager.components import SystemComponents
from typing import Tuple, Union, Sequence
from pygame.math import Vector2
from pygame.color import Color

Coordinate = Union[Tuple[float, float], Sequence[float], Vector2]
RGBAOutput = Tuple[int, int, int, int]
ColorValue = Union[Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]

class Window(SystemComponents):
    """
    Window class

    Create a pygame window and it has the windows methods.
    clear(): Clear the window (paint to the bg_colour)
    update(): Update the clock with the FPS and flip the window
    get_dt(): Get the delta time (the time elapsed since the last update)
     
    """
    def __init__(self, window_size: Coordinate, fullscreen: int,
                 caption: str, fps: int, bg_colour: ColorValue):
        SystemComponents.__init__(self)
        pygame.init()
        self.fps = fps
        self.background_colour = bg_colour
        self.window_size = window_size
        self.start_time = time.time()

        self.screen: pygame.Surface = pygame.display.set_mode(window_size, fullscreen)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()

        self.previous_frame = time.time()

    def get_dt(self):
        dt: float = time.time() - self.previous_frame
        self.previous_frame = time.time()
        return dt

    def update(self):
        self.clock.tick(self.fps)
        
    def clear(self):
        self.screen.fill(self.background_colour)
        
    def swap_buffers(self):
        pygame.display.flip()






