import pygame
from ..element_manager.components import SystemComponents
from .assets import Assets
from .camera import Camera
from .input import KeyboardInput
from .input import MouseInput
from .render import Render
from .window import Window


class Game(SystemComponents):
    """
    Parent Game class
    The main Game class should inherit from this
    class and override its methods
    """
    
    def __init__(self):
        SystemComponents.__init__(self)
        self.window: Window
        self.render: Render
        self.assets: Assets
        self.camera: Camera
        self.mouseinput: MouseInput
        self.keyboardinput: KeyboardInput
        

    def load_data(self):
        pass

    def game_loop(self):
        pass

    def run(self):
        self.playing = True
        self.load_data()
        while self.playing:
            self.game_loop()


