from src.FarmGame.main.configs.game_config import GameConfig


class BuildConfig(GameConfig):
  """Build Configs"""
  window_width = 1280
  window_height = 720
  title = f'PyFarm - Version: {GameConfig.version}'
  fullscreen = 0
  cheats = True

  # World settings
  map_width = 10
  map_height = 10
  tile_width = 96
  tile_height = 96
  scale_factor = 1
