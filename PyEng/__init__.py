from PyEng.element_manager.components import GameComponent, SystemComponent
from PyEng.shared.types import ColorValue, Coordinate
from PyEng.system.assets import Assets
from PyEng.system.camera import Camera
from PyEng.system.game import Game
from PyEng.system.input import KeyboardInput, MouseInput
from PyEng.system.render import Render
from PyEng.system.window import Window


def init(
    *,
    window_size: Coordinate = (640, 480),
    fullscreen: int = 0,
    caption: str = "My Window",
    fps: int = 60,
    bg_colour: ColorValue = (0, 0, 0),
    assets_folder: str = "data",
    key_mapping: str = "config",
):
  """Initialise all the system components"""

  Window(window_size, fullscreen, caption, fps, bg_colour)
  Render()
  Assets(assets_folder)
  Camera()
  MouseInput(key_mapping)
  KeyboardInput(key_mapping)
