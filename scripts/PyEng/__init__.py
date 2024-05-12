from .element_manager.components import SystemComponents, GameComponents, components_manager
from .system.assets import Assets
from .system.camera import Camera
from .system.game import Game
from .system.input import KeyInput
from .system.input import MouseInput
from .system.render import Render
from .system.window import Window


def init(window_size=(640, 480), fullscreen=False, caption="My Window", fps=60, bg_colour=(0, 0, 0), assets_folder="data", game_type="default"):
    Window(window_size, fullscreen, caption, fps, bg_colour)
    Render(game_type)
    Assets(assets_folder)
    Camera()
    MouseInput()
    KeyInput()

