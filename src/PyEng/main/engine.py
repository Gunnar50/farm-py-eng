import os
from PyEng.components.frame_timer import FrameTimer
from PyEng.components.keyboard import Keyboard
from PyEng.components.mouse import Mouse
from PyEng.components.state_manager import StateManager
from PyEng.components.window import Window
from PyEng.main.engine_config import EngineConfigs
from PyEng.gui.ui_components.user_interface import UserInterface
from PyEng.main.engine_files import EngineFiles
from PyEng.utils.debugger import Debugger
from PyEng.utils.error_manager import ErrorManager
from PyEng.utils.exceptions import IllegalStateException


class Engine:

  __instance = None

  def __init__(
      self,
      window: Window,
      mouse: Mouse,
      keyboard: Keyboard,
      timer: FrameTimer,
      state_manager: StateManager,
  ):
    self.window = window
    self.mouse = mouse
    self.keyboard = keyboard
    self.timer = timer
    self.state_manager = state_manager
    self.close_flag = False

  def update(self) -> None:
    # BackgroundLoader.do_top_gl_requests()
    # UserInterface.update(self.get_delta())
    self.keyboard.update()
    self.mouse.update()
    self.window.update()
    self.timer.update()
    self.state_manager.update()

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
      raise IllegalStateException("Engine has already been initialised!")

    return EngineCreator(configs).get_instance()


class EngineCreator:

  def __init__(self, configs: EngineConfigs):
    # TODO add res folder
    self.check_assets_folder_exists()

    # Create gloabal systems
    ErrorManager(EngineFiles.ERROR_FOLDER)
    Debugger(configs.debugger)
    # BackgroundLoader()

    # Create engine instance
    self.engine = self.create_engine_instance(configs)

  def get_instance(self) -> 'Engine':
    return self.engine

  def check_assets_folder_exists(self):
    if os.path.exists(EngineFiles.ASSETS_FOLDER):
      return
    raise IllegalStateException("Can't init engine - assets folder not found.")

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
    mouse = Mouse(window)
    timer = FrameTimer(configs.fps)
    state_manager = StateManager()
    # Create UI
    UserInterface(
        window,
        mouse,
        keyboard,
        configs.ui_configs,
    )
    return Engine(
        window,
        mouse,
        keyboard,
        timer,
        state_manager,
    )
