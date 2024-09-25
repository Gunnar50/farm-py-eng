import os

from src.PyEng.components.components import ComponentManager
from src.PyEng.components.input import Keyboard, Mouse
from src.PyEng.components.window import Window
from src.PyEng.main.engine_config import EngineConfigs
from src.PyEng.main.engine_files import EngineFiles
from src.PyEng.utils.debugger import Debugger
from src.PyEng.utils.error_manager import ErrorManager
from src.shared import exceptions
from src.shared.debug import LOGGER


class Engine:

  __instance = None

  def __init__(
      self,
      window: Window,
      mouse: Mouse,
      keyboard: Keyboard,
  ):
    self.components_manager = ComponentManager()
    self.window = window
    self.mouse = mouse
    self.keyboard = keyboard
    self.close_flag = False

  def update(self) -> None:
    self.components_manager.update()

  def get_delta(self) -> float:
    return self.timer.get_delta()

  def get_current_time(self) -> float:
    return self.timer.get_time()

  def close_engine(self) -> None:
    # BackgroundLoader.clean_up()
    # Ui.clean_up()
    self.window.destroy()

  @classmethod
  def create(
      cls,
      configs: EngineConfigs = EngineConfigs.get_default_configs(),
  ) -> 'Engine':
    if cls.__instance is not None:
      raise exceptions.IllegalStateException(
          'Engine has already been initialised!')

    return EngineCreator(configs).get_instance()


class EngineCreator:

  def __init__(self, configs: EngineConfigs):
    if not os.path.exists(EngineFiles.ASSETS_FOLDER):
      raise exceptions.IllegalStateException(
          f"Can't init engine - assets folder not found in root directory {EngineFiles.ROOT_FOLDER}."
      )

    # Create gloabal systems
    ErrorManager(EngineFiles.ERROR_FOLDER)
    Debugger(configs.debugger)
    # BackgroundLoader()

    # Create engine instance
    self.engine = self.create_engine_instance(configs)

  def get_instance(self) -> 'Engine':
    return self.engine

  def create_engine_instance(self, configs: EngineConfigs):
    window = Window(
        window_width=configs.window_width,
        window_height=configs.window_height,
        fullscreen=configs.fullscreen,
        caption=configs.caption,
        fps=configs.fps,
        vsync=configs.vsync,
        background_colour=configs.background_colour,
    )
    keyboard = Keyboard()
    mouse = Mouse()
    # timer = FrameTimer(configs.fps)
    # state_manager = StateManager()
    # Create UI
    # UserInterface(
    #     window,
    #     mouse,
    #     keyboard,
    #     configs.ui_configs,
    # )
    return Engine(
        window,
        mouse,
        keyboard,
    )
