import os

from src.PyEng.components.components import ComponentManager
from src.PyEng.components.input import Input
from src.PyEng.components.state_manager import StateManager
from src.PyEng.components.window import Window
from src.PyEng.main.engine_config import EngineConfigs
from src.PyEng.main.engine_files import EngineFiles
from src.PyEng.utils.debugger import Debugger
from src.PyEng.utils.error_manager import ErrorManager
from src.shared import exceptions
from src.shared.debug import LOGGER


class Engine:
  __instance = None

  def __init__(self, configs: type[EngineConfigs]):
    self.window: Window
    self.input: Input
    self.components_manager = ComponentManager()

    self.check_assets_folder()
    self.create_global_components(configs)
    self.create_engine_components(configs)

    self.close_flag = False

    Engine.__instance = self

  @classmethod
  def get_instance(cls) -> 'Engine':
    if cls.__instance is None:
      return cls.create()
    return cls.__instance

  def update(self) -> None:
    self.components_manager.update()

  def render(self) -> None:
    self.renderer.render()

  def check_assets_folder(self):
    if not os.path.exists(EngineFiles.ASSETS_FOLDER):
      raise exceptions.IllegalStateException(
          f"Can't create engine - assets folder not found in root directory: {EngineFiles.ROOT_FOLDER}."
      )

  def create_global_components(self, configs: type[EngineConfigs]):
    # Create global systems
    ErrorManager(EngineFiles.ERROR_FOLDER)
    Debugger(configs.debugger)
    # BackgroundLoader()

  def create_engine_components(self, configs: type[EngineConfigs]):
    # Create engine components
    self.window = Window(
        window_width=configs.window_width,
        window_height=configs.window_height,
        fullscreen=configs.fullscreen,
        caption=configs.title,
        fps=configs.fps,
        vsync=configs.vsync,
        background_colour=configs.background_colour,
    )
    # Set up keyboard and mouse inputs
    self.input = Input(EngineFiles.KEY_MAPPINGS)
    self.state_manager = StateManager(configs.default_state,
                                      configs.initial_state)
    # self.timer = FrameTimer(configs.fps)

    # Create UI
    # UserInterface(
    #     self.window,
    #     self.mouse,
    #     self.keyboard,
    #     configs.ui_configs,
    # )

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
      configs: type[EngineConfigs] = EngineConfigs.get_default_configs(),
  ) -> 'Engine':
    if cls.__instance is not None:
      raise exceptions.IllegalStateException(
          'Engine has already been initialised!')

    return cls(configs)
