from .element_manager.components import SystemComponents, GameComponents, components_manager
from .system.assets import Assets
from .system.game import Game
from .system.camera import Camera
from .system.input import KeyboardInput
from .system.input import MouseInput
from .system.render import Render
from .system.window import Window
from .types import Coordinate, ColorValue, StrPath


def init(*, window_size: Coordinate = (640, 480),
         fullscreen: int = 0, 
         caption: str = "My Window",
         fps: int = 60,
         bg_colour: ColorValue = (0, 0, 0), 
         assets_folder: StrPath = "data",
         key_mapping: StrPath = "config"
         ):
    
    """Initialise all the system components"""

    Window(window_size, fullscreen, caption, fps, bg_colour)
    Render()
    Assets(assets_folder)
    Camera()
    MouseInput(key_mapping)
    KeyboardInput(key_mapping)

