from src.FarmGame.main.configs.game_config import GameConfig


class BuildConfig(GameConfig):
  """Build Configs"""

  def __init__(self) -> None:
    GameConfig.__init__(self)
    self.window_width = 1280
    self.window_height = 720
    self.title = f'PyFarm - Version: {self.version}'
    self.fullscreen = 0
    self.cheats = True
