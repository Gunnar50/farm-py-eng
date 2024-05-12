import pygame
from ..element_manager.components import SystemComponents


class Game(SystemComponents):
    """
    Parent Game class
    The main Game class should inherit from this
    class and override its methods
    """
    
    def __init__(self):
        SystemComponents.__init__(self)

    def load_data(self):
        pass

    def game_loop(self):
        pass

    def run(self):
        self.playing = True
        self.load_data()
        while self.playing:
            self.game_loop()


