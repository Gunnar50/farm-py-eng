from .element_manager.components import SystemComponents, GameComponents, components_manager
from .system.assets import Assets
from .system.game import Game
from .system.camera import Camera
from .system.input import KeyboardInput
from .system.input import MouseInput
from .system.render import Render
from .system.window import Window
from typing import Literal


def init(window_size=(640, 480), fullscreen=0, 
         caption="My Window", fps=60, bg_colour=(0, 0, 0), 
         assets_folder="data", game_type: Literal["default", "isometric"]="default"):
    Window(window_size, fullscreen, caption, fps, bg_colour)
    Render(game_type)
    Assets(assets_folder)
    Camera()
    MouseInput()
    KeyboardInput()

