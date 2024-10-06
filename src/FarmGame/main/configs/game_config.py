from src.FarmGame.main.game_state import GameState
from src.PyEng.main.engine_config import EngineConfigs
from src.shared.version import Version


class GameConfig(EngineConfigs):
  """Game Configs"""

  def __init__(self) -> None:
    self.version = Version(0, 0, 0)
    self.game_speed = 1
    self.cheats = True
    self.show_debug = True
    self.auto_save = True
    self.session_creator = NotImplemented
    self.initial_state = GameState.INITIAL
    self.default_state = GameState.NORMAL
